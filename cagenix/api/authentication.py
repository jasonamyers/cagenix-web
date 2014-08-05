import base64
import datetime
import hashlib
import hmac
import time

from dateutil import parser as date_parser
from functools import wraps
from urllib import unquote_plus, quote_plus, unquote
from urlparse import urlparse

from flask import request, jsonify

from cagenix.users.models import User


def parse_qs(qs, keep_blank_values=0, strict_parsing=0):
    """Parse a query given as a string argument.
    Arguments:

    qs: percent-encoded query string to be parsed

    keep_blank_values: flag indicating whether blank values in
        percent-encoded queries should be treated as blank strings.  A
        true value indicates that blanks should be retained as blank
        strings.  The default false value indicates that blank values
        are to be ignored and treated as if they were  not included.

    strict_parsing: flag indicating what to do with parsing errors. If
        false (the default), errors are silently ignored. If true,
        errors raise a ValueError exception.

    Returns a dictionary.
    """
    pairs = [s2 for s1 in qs.split('&') for s2 in s1.split(';')]
    r = []
    for name_value in pairs:
        if not name_value and not strict_parsing:
            continue
        nv = name_value.split('=', 1)
        if len(nv) != 2:
            if strict_parsing:
                raise ValueError('bad query field: %r' % name_value)
            # Handle case of a control-name with no equal sign
            if keep_blank_values:
                nv.append('')
            else:
                continue
        if len(nv[1]) or keep_blank_values:
            name = nv[0]
            value = nv[1]
            r.append((name, value))

    return dict(r)


def smush_qs(query):
    l = []
    for k, v in sorted(query.items(), key=lambda i: i[0].lower()):
        l.append('%s=%s' % (k, v))
    return '&'.join(l)


def generate_signature(secret, qs):
    """
        secret- key used to sign request
        qs - raw query_string

        returns signature(string) based on params and secret key
    """
    secret = secret.encode('utf-8')
    query_string = qs.encode('utf-8')
    digest = hmac.new(secret, query_string, hashlib.sha512).digest()
    sig = base64.b64encode(digest)
    return sig


def generate_qs(user):
    """
        user - unique User identifier

        returns encoded query string
    """
    ts = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
    params = {
        'email': quote_plus(user.email),
        'timestamp': quote_plus(ts),
    }
    qs = smush_qs(params)
    signature = generate_signature(user.secret, qs)
    params['code'] = signature
    return smush_qs(params)


def check_signature(secret_key, query_string, max_age_in_seconds=5):
    """
        secret_key - secret_key used to validate request
        query_string - query_string passed from request
        max_age_in_seconds - max age of request

        returns True or exception
    """
    params = parse_qs(query_string)
    now = datetime.datetime.utcnow()
    ts = unquote_plus(params.get('timestamp', ''))
    then = date_parser.parse(ts, ignoretz=True)
    delta = now - then
    if delta.total_seconds() > max_age_in_seconds:
        return False, 'Signature expired'
    request_sig = params.pop('code', '')
    query_string = smush_qs(params)
    generated_sig = generate_signature(secret_key, query_string)
    if not unquote(request_sig) == generated_sig:
        return False, 'Invalid Signature'
    return True, None


def authenticate_get_request(*arg, **kwargs):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ''' authenticate_request validates the use of the provided credentials.
            It cycles through a tuple of required_headers and checks the presence
            of each header for validation. It then validates the licensekey and
            will allow the consumer to use the decorated handler
            '''
            user = User.by_email(request.args.get('email'))
            if not user or not user.active or not user.activated:
                response = jsonify(request=None, response={'error': 'Invalid Practitioner'})
                response.status_code = 403
                return response

            query_string = urlparse(request.url).query

            is_valid_sig, message = check_signature(user.secret, query_string)

            if not is_valid_sig:
                response = jsonify(request=None, response={'error': 'Invalid Practitioner'})
                response.status_code = 403
                return response

            return f(*args, **kwargs)
        return decorated_function
    return decorator


def authenticate_request(*args, **kwargs):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ''' authenticate_request validates the use of the provided credentials.
            It cycles through a tuple of required_headers and checks the presence
            of each header for validation. It then validates the licensekey and
            will allow the consumer to use the decorated handler
            '''

            required_headers = ('datetime', 'body_hash', 'key', 'signature')
            for header in required_headers:
                if header not in request.headers:
                    response = jsonify(request=request.json, response={'error': 'Required headers missing'})
                    response.status_code = 403
                    return response

            sent_timestamp = request.headers.get('datetime', '')
            sent_body_hash = request.headers.get('body_hash', '')
            sent_key = request.headers.get('key', '')
            sent_signature = request.headers.get('signature', '')

            user = User.by_email(sent_key)
            if not user or not user.active or not user.activated:
                response = jsonify(request=request.json, response={'error': 'Invalid Practitioner'})
                response.status_code = 403
                return response

            recreated_signature = hashlib.sha256(unicode(sent_body_hash + sent_timestamp + user.secret)).hexdigest()

            if not sent_signature == recreated_signature:
                response = jsonify(request=request.json, response={'error': 'Invalid Practitioner'})
                response.status_code = 403
                return response

            return f(*args, **kwargs)
        return decorated_function
    return decorator
