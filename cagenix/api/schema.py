"""cagenix.api.schema

This file defines the schema used to validate json requests to the API blueprint.
"""

PRACTITIONERS_CREATE = {
    'type': 'object',
    'properties': {
        'first_name': {'type': 'string', 'required': True},
        'last_name': {'type': 'string', 'required': True},
        'address_one': {'type': 'string', 'required': True},
        'address_two': {'type': 'string', 'required': False},
        'city': {'type': 'string', 'required': True},
        'state': {'type': 'string', 'required': True},
        'zip_code': {'type': 'string', 'required': True},
        'email': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
        'activation_code': {'type': 'string', 'required': True},
        'primary_color': {'type': 'string', 'required': False},
        'secondary_color': {'type': 'string', 'required': False},
        'practice': {'type': 'integer', 'required': False}
    },
    'additionalProperties': False,
}

PRACTITIONERS_EDIT = {
    'type': 'object',
    'properties': {
        'first_name': {'type': 'string', 'required': True},
        'last_name': {'type': 'string', 'required': True},
        'address_one': {'type': 'string', 'required': True},
        'address_two': {'type': 'string', 'required': False},
        'city': {'type': 'string', 'required': True},
        'state': {'type': 'string', 'required': True},
        'zip_code': {'type': 'string', 'required': True},
        'email': {'type': 'string', 'required': True},
        'primary_color': {'type': 'string', 'required': False},
        'secondary_color': {'type': 'string', 'required': False},
        'practice': {'type': 'integer', 'required': False},
        'active': {'type': 'boolean', 'required': False}
    },
    'additionalProperties': False,
}

PRACTITIONERS_DELETE = {
    'type': 'object',
    'properties': {
        'practitioner_id': {'type': 'integer', 'required': True},
    },
    'additionalProperties': False,
}

PRACTITIONERS_LOGIN = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
    },
    'additionalProperties': False,
}

PATIENTS_CREATE = {
    'type': 'object',
    'properties': {
        'first_name': {'type': 'string', 'required': True},
        'last_name': {'type': 'string', 'required': True},
        'address_one': {'type': 'string', 'required': True},
        'address_two': {'type': 'string', 'required': False},
        'city': {'type': 'string', 'required': True},
        'state': {'type': 'string', 'required': True},
        'zip_code': {'type': 'string', 'required': True},
        'email': {'type': 'string', 'required': True},
        'practice_id': {'type': 'integer', 'required': False},
        'dentist_id': {'type': 'integer', 'required': False}
    },
    'additionalProperties': False,
}

PATIENTS_EDIT = {
    'type': 'object',
    'properties': {
        'first_name': {'type': 'string', 'required': True},
        'last_name': {'type': 'string', 'required': True},
        'address_one': {'type': 'string', 'required': True},
        'address_two': {'type': 'string', 'required': False},
        'city': {'type': 'string', 'required': True},
        'state': {'type': 'string', 'required': True},
        'zip_code': {'type': 'string', 'required': True},
        'email': {'type': 'string', 'required': True},
        'choice_one': {'type': 'string', 'required': False, 'blank': True},
        'choice_two': {'type': 'string', 'required': False, 'blank': True},
        'choice_three': {'type': 'string', 'required': False, 'blank': True},
        'practice_id': {'type': 'integer', 'required': False},
        'dentist_id': {'type': 'integer', 'required': False},
        'active': {'type': 'boolean', 'required': False}
    },
    'additionalProperties': False,
}

PATIENTS_DELETE = {
    'type': 'object',
    'properties': {
        'patient_id': {'type': 'integer', 'required': True},
    },
    'additionalProperties': False,
}
