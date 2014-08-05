from functools import wraps

from flask import request, jsonify

import validictory


def validate_api_request(json_schemas, *args, **kwargs):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ''' validate_request checks the content-type of the request
            and ensures its application/json. Afterwards it uses the validictory
            library to validate the request against a json schema mapped in
            json_schemas. If the validation fails validictory will throw an
            ValueError exception, and the handler will return a 400 response.
            '''

            # validating content-type, returning request.data on purpose
            # if the request isn't json, request.json is NoneType
            if (not request.headers
                or not 'content-type' in request.headers
                    or not 'application/json' in request.headers['content-type']):

                response = jsonify(request=request.json,
                    response={'error': ('Content-type not set or '
                    'Content-type not application/json')})
                response.status_code = 405

                return response

            try:
                validictory.validate(request.json, json_schemas[request.method])
            except ValueError as e:
                request.json.pop('password', None)
                response = jsonify(request=request.json, response={'error': e.message})
                response.status_code = 400
                return response

            data = dict(request.json)
            errors = []

            for key in data:
                if isinstance(data[key], str):
                    if len(data[key]) > 250:
                        errors.append({
                            'error': 'Field exceeds 250 characters.',
                            'key': key,
                            'value': data[key],
                        })

            if errors.__len__() > 0:
                response = jsonify(request=request.json, response=errors)
                response.status_code = 400
                return response

            return f(*args, **kwargs)
        return decorated_function
    return decorator
