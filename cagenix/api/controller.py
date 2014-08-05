"""cagenix.api.controller

This file defines the URL routes and controller logic for the API blueprint.
"""
import logging
import json

from flask import Blueprint, request, jsonify
from flask_security.utils import encrypt_password, verify_password

from .validation import validate_api_request
from .authentication import authenticate_request, authenticate_get_request
from .schema import (
    PRACTITIONERS_CREATE, PRACTITIONERS_LOGIN, PRACTITIONERS_EDIT, PRACTITIONERS_DELETE,
    PATIENTS_CREATE, PATIENTS_DELETE, PATIENTS_EDIT
)

from cagenix import db
from cagenix.users.models import User
from cagenix.patients.models import Patient

log = logging.getLogger(__name__)
mod = Blueprint('api', __name__, url_prefix='/api')


@mod.route('/v1/practitioners/create', methods=['POST'])
@validate_api_request(json_schemas={'POST': PRACTITIONERS_CREATE})
def practitioners_create(*args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.data)
        user = User.by_email(data['email'])
        if not user or user.activated:
            response = jsonify(
                request=request.json,
                response={'error': 'Practitioner or Activiation Code does not exist.'})
            response.status_code = 404
            return response

        if not user.activation_code == data['activation_code']:
            response = jsonify(
                request=request.json,
                response={'error': 'Bad activation code.'})
            response.status_code = 401
            return response
        else:
            user.map_data(data)
            user.password = encrypt_password(data['password'])
            user.gen_secret()
            user.activated = True
            db.session.add(user)
            db.session.commit()
            data.pop('password')
            response = jsonify(
                request=data,
                response={'practitioner_id': user.id})
            response.status_code = 201
            return response
    else:
        response = jsonify(
            request=request.json,
            response={'error': 'This request type not supported'})
        response.status_code = 400
        return response


@mod.route('/v1/practitioners/<user_id>', methods=['PUT', 'DELETE'])
@authenticate_request()
@validate_api_request(json_schemas={'PUT': PRACTITIONERS_EDIT, 'DELETE': PRACTITIONERS_DELETE})
def practitioners_edit(*args, **kwargs):
    print request.method
    if request.method == 'PUT':
        data = json.loads(request.data)
        user = User.by_id(kwargs.get('user_id'))
        if not user or not user.activated:
            response = jsonify(
                request=request.json,
                response={'error': 'Invalid Practitioner.'})
            response.status_code = 404
            return response

        user.map_data(data)
        db.session.add(user)
        db.session.commit()
        response = jsonify(
            request=data,
            response={
                'practitioner_id': user.id,
                'active': user.active
            }
        )
        response.status_code = 200
        return response
    elif request.method == 'DELETE':
        data = json.loads(request.data)
        user = User.by_id(int(kwargs.get('user_id')))
        requester = User.by_email(request.headers.get('key'))
        if user == requester:
            status = 'Success'
            status_code = 200
            db.session.delete(user)
            db.session.commit()
        else:
            status = 'Not Authorized'
            status_code = 401

        response = jsonify(
            request=data,
            response={
                'status': status
            }
        )
        response.status_code = status_code
        return response
    else:
        print request.method
        response = jsonify(
            request=request.json,
            response={'error': 'This request type not supported'})
        response.status_code = 400
        return response


@mod.route('/v1/practitioners/<user_id>', methods=['GET'])
@authenticate_get_request()
def practitioners_get(*args, **kwargs):
    user = User.by_id(kwargs.get('user_id'))
    if not user or not user.activated:
        response = jsonify(
            request=request.json,
            response={'error': 'Invalid Practitioner.'})
        response.status_code = 404
        return response

    practice = None
    if user.practice:
        practice = practice.id

    response = jsonify(
        request={
            'practitioner_id': user.id,
        },
        response={
            'active': user.active,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address_one': user.address_one,
            'address_two': user.address_two,
            'city': user.city,
            'state': user.state,
            'zip_code': user.zip_code,
            'email': user.email,
            'activation_code': user.activation_code,
            'primary_color': user.primary_color,
            'secondary_color': user.secondary_color,
            'practice': practice,
        }
    )
    response.status_code = 200
    return response


@mod.route('/v1/practitioners/login', methods=['POST'])
@validate_api_request(json_schemas={'POST': PRACTITIONERS_LOGIN})
def practitioners_login(*args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.data)
        user = User.by_email(data['email'])
        if not user or not user.activated:
            data.pop('password')
            response = jsonify(
                request=data,
                response={'error': 'Invalid Practitioner'})
            response.status_code = 404
            return response

        if not verify_password(data['password'], user.password):
            data.pop('password')
            response = jsonify(
                request=data,
                response={'error': 'Authentication Failed'})
            response.status_code = 401
            return response
        else:
            data.pop('password')
            response = jsonify(
                request=data,
                response={'secret': user.secret})
            response.status_code = 200
            return response
    else:
        response = jsonify(
            request=request.json,
            response={'error': 'This request type not supported'})
        response.status_code = 400
        return response


@mod.route('/v1/patients/create', methods=['POST'])
@validate_api_request(json_schemas={'POST': PATIENTS_CREATE})
def patients_create(*args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.data)
        patient = Patient()
        patient.map_data(data)
        db.session.add(patient)
        db.session.commit()
        print data
        response = jsonify(
            request=data,
            response={'patient_id': patient.id})
        response.status_code = 201
        return response
    else:
        response = jsonify(
            request=request.json,
            response={'error': 'This request type not supported'})
        response.status_code = 400
        return response


@mod.route('/v1/patients/<patient_id>', methods=['PUT', 'DELETE'])
@authenticate_request()
@validate_api_request(json_schemas={'PUT': PATIENTS_EDIT, 'DELETE': PATIENTS_DELETE})
def patients_edit(*args, **kwargs):
    print request.method
    if request.method == 'PUT':
        data = json.loads(request.data)
        patient = Patient.by_id(kwargs.get('patient_id'))
        if not patient:
            response = jsonify(
                request=request.json,
                response={'error': 'Invalid Patient.'})
            response.status_code = 404
            return response

        patient.map_data(data)
        db.session.add(patient)
        db.session.commit()
        response = jsonify(
            request=data,
            response={
                'patient_id': patient.id,
                'active': patient.active
            }
        )
        response.status_code = 200
        return response
    elif request.method == 'DELETE':
        data = json.loads(request.data)
        patient = Patient.by_id(int(kwargs.get('patient_id')))
        if patient:
            status = 'Success'
            status_code = 200
            db.session.delete(patient)
            db.session.commit()
        else:
            status = 'Not Authorized'
            status_code = 401

        response = jsonify(
            request=data,
            response={
                'status': status
            }
        )
        response.status_code = status_code
        return response
    else:
        print request.method
        response = jsonify(
            request=request.json,
            response={'error': 'This request type not supported'})
        response.status_code = 400
        return response


@mod.route('/v1/patients/<patient_id>', methods=['GET'])
@authenticate_get_request()
def patients_get(*args, **kwargs):
    patient = Patient.by_id(kwargs.get('patient_id'))
    if not patient:
        response = jsonify(
            request=request.json,
            response={'error': 'Invalid Patient.'})
        response.status_code = 404
        return response

    response = jsonify(
        request={
            'patient_id': patient.id,
        },
        response={
            'active': patient.active,
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'address_one': patient.address_one,
            'address_two': patient.address_two,
            'city': patient.city,
            'state': patient.state,
            'zip_code': patient.zip_code,
            'email': patient.email,
            'choice_one': patient.choice_one,
            'choice_two': patient.choice_two,
            'choice_three': patient.choice_three,
            'practice': patient.practice.id,
            'practitioner': patient.dentist.id,
        }
    )
    response.status_code = 200
    return response
