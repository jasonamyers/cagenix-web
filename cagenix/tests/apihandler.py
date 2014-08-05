'''This file contains all the functions that are used to support the API
tests.'''

import json
import requests
from hashlib import sha256
from datetime import datetime
EMAIL = ''
API_SECRET = ''
SESSION = ''


def make_headers(data, email=EMAIL, api_secret=API_SECRET):
    '''This function creates the headers required to interact with the API

    :param data: the data contained in the request body
    :param email: the email, if not supplied the glocal one is used

    :param api_secret: the API secret, if not supplied the one in


    :type data: dict
    :type api_key: string
    :type api_secret: string
    :returns: headers
    :rtype: dict
    '''
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    body_hash = json.dumps(data, separators=(',', ':'), sort_keys = True)
    body_hash = sha256(unicode(body_hash)).hexdigest()
    signature = sha256(unicode(body_hash + timestamp + api_secret)).hexdigest()

    headers = {
        'content-type': 'application/json',
        'body_hash': body_hash,
        'lang': 'en',
        'key': email,
        'signature': signature,
        'datetime': timestamp,
    }
    return headers


def make_post_request(headers, data, api_url):
    '''This function makes a HTTP POST request to the API with the proper auth

    :param headers: The HTTP headers for the request
    :param data: the data contained in the request body
    :param api_url: the url to which the request is made
    :type headers: dict
    :type data: dict
    :type api_url: string
    :returns: request.status_code, request.text, number
    :rtype: int, string, string
    '''
    data = json.dumps(data)
    request = requests.post(api_url, headers=headers, data=data)
    return request.status_code, request.text


def make_put_request(headers, data, api_url):
    '''This function makes a HTTP POST request to the API with the proper auth

    :param headers: The HTTP headers for the request
    :param data: the data contained in the request body
    :param api_url: the url to which the request is made
    :type headers: dict
    :type data: dict
    :type api_url: string
    :returns: request.status_code, request.text, number
    :rtype: int, string, string
    '''
    data = json.dumps(data)
    request = requests.put(api_url, headers=headers, data=data)
    return request.status_code, request.text


def make_get_request(user, api_url):
    from cagenix.api.authentication import generate_qs
    qs = generate_qs(user)
    request = requests.get(api_url + qs)
    return request.status_code, request.text


def make_delete_request(headers, data, api_url):
    data = json.dumps(data)
    request = requests.delete(api_url, headers=headers, data=data)
    return request.status_code, request.text
