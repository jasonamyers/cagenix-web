############
Patients API
############


Create a patient
================
This endpoint is used to create a patient in the Cagenix API.

.. note:: **POST** /api/v1/patients/create

Call
----

.. code-block:: js

    {
        'first_name': '',
        'last_name': '',
        'address_one': '',
        'address_two': '',
        'city': '',
        'state': '',
        'zip_code': '',
        'email': '',
        'practice': '',
        'practitioner': '',
    }



+----------------------+-----------------------------------+--------+----------+
| Property             | Description                       | Type   | Required |
+======================+===================================+========+==========+
| first_name           | First Name                        | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| last_name            | Last Name                         | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| address_one          | First address line                | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| address_two          | Second address line               | String |          |
+----------------------+-----------------------------------+--------+----------+
| city                 | City                              | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| state                | State                             | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| zip_code             | ZIP Code in 5-4 format            | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| email                | email address                     | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| practice             | ID of the Practice                | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| practitioner         | ID of the Practitioner            | Integer|    X     |
+----------------------+-----------------------------------+--------+----------+

Response
--------

.. code-block:: js

    {
        'request': {
            'first_name': '',
            'last_name': '',
            'address_one': '',
            'address_two': '',
            'city': '',
            'state': '',
            'zip_code': '',
            'email': '',
            'practice': '',
            'practitioner': '',
        },
        'response': {
            'patient_id': '',
        },
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the Patient ID  | Object |
+----------------------+-----------------------------------+--------+
| patient_id           | A unique ID for the Patient record| Integer|
+----------------------+-----------------------------------+--------+


Retrieve Patient details
========================
This endpoint is used to retrieve all the details of a Patient.

.. note:: **GET** /api/v1/patients/<ID>

Response
--------

.. code-block:: js

    {
        'request': {
            'patient_id': '',
        },
        'response': {
            'active': '',
            'first_name': '',
            'last_name': '',
            'address_one': '',
            'address_two': '',
            'city': '',
            'state': '',
            'zip_code': '',
            'email': '',
            'choice_one': '',
            'choice_two': '',
            'choice_three': '',
            'practice': '',
            'practitioner': '',
        }
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| active               | Active Flag for Archiving         | String |
+----------------------+-----------------------------------+--------+
| first_name           | First Name                        | String |
+----------------------+-----------------------------------+--------+
| last_name            | Last Name                         | String |
+----------------------+-----------------------------------+--------+
| address_one          | First address line                | String |
+----------------------+-----------------------------------+--------+
| address_two          | Second address line               | String |
+----------------------+-----------------------------------+--------+
| city                 | City                              | String |
+----------------------+-----------------------------------+--------+
| state                | State                             | String |
+----------------------+-----------------------------------+--------+
| zip_code             | ZIP Code in 5-4 format            | String |
+----------------------+-----------------------------------+--------+
| email                | email address                     | String |
+----------------------+-----------------------------------+--------+
| choice_one           | The "best" choice                 | String |
+----------------------+-----------------------------------+--------+
| choice_two           | The "better" choice               | String |
+----------------------+-----------------------------------+--------+
| choice_three         | The "good" choice                 | String |
+----------------------+-----------------------------------+--------+
| practice             | ID of the Practice                | Integer|
+----------------------+-----------------------------------+--------+
| practitioner         | ID of the Practitioner            | Integer|
+----------------------+-----------------------------------+--------+

Update a patient
================
This endpoint is used to update a patient in the Cagenix API.

.. note:: **PUT** /api/v1/patients/<id>

Call
----

.. code-block:: js

    {
        'first_name': '',
        'last_name': '',
        'address_one': '',
        'address_two': '',
        'city': '',
        'state': '',
        'zip_code': '',
        'email': '',
        'active': '',
        'practice': '',
        'practitioner': '',
    }


+----------------------+-----------------------------------+--------+----------+
| Property             | Description                       | Type   | Required |
+======================+===================================+========+==========+
| active               | Active Flag for Archiving         | Boolean|          |
+----------------------+-----------------------------------+--------+----------+
| patient_id           | Patient ID                        | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| first_name           | First Name                        | String |          |
+----------------------+-----------------------------------+--------+----------+
| last_name            | Last Name                         | String |          |
+----------------------+-----------------------------------+--------+----------+
| address_one          | First address line                | String |          |
+----------------------+-----------------------------------+--------+----------+
| address_two          | Second address line               | String |          |
+----------------------+-----------------------------------+--------+----------+
| city                 | City                              | String |          |
+----------------------+-----------------------------------+--------+----------+
| state                | State                             | String |          |
+----------------------+-----------------------------------+--------+----------+
| zip_code             | ZIP Code in 5-4 format            | String |          |
+----------------------+-----------------------------------+--------+----------+
| email                | email address                     | String |          |
+----------------------+-----------------------------------+--------+----------+
| active               | Active Flag for Archiving         | Boolean|          |
+----------------------+-----------------------------------+--------+----------+
| practice             | ID of the Practice                | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| practitioner         | ID of the Practitioner            | Integer|          |
+----------------------+-----------------------------------+--------+----------+

Response
--------

.. code-block:: js

    {
        'request': {
            'patient_id': '',
            'first_name': '',
            'last_name': '',
            'address_one': '',
            'address_two': '',
            'city': '',
            'state': '',
            'zip_code': '',
            'email': '',
            'active': '',
            'practice': '',
            'practitioner': '',
        },
        'response': {
            'patient_id': '',
            'active': '',
        },
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the Patient ID  | Object |
+----------------------+-----------------------------------+--------+
| patient_id           | A unique ID for the Patient record| Integer|
+----------------------+-----------------------------------+--------+
| active               | Active Flag for Archiving         | Boolean|
+----------------------+-----------------------------------+--------+

Delete a patient
================
This endpoint is used to Delete a patient in the Cagenix API.

.. note:: **DELETE** /api/v1/patients/<id>

Response
--------

.. code-block:: js

    {
        'request': {
            'patient_id': '',
        },
        'response': {
            'status': '',
        },
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the Patient ID  | Object |
+----------------------+-----------------------------------+--------+
| status               | The result of the DELETE          | String |
|                      | opperation (EX: Success, Failed)  |        |
+----------------------+-----------------------------------+--------+
