###############
Evaluations API
###############


Create an Evaluation
====================
This endpoint is used to create an evaluation in the Cagenix API.

.. note:: **POST** /api/v1/evaluations/create

Call
----

.. code-block:: js

    {
        'practice': '',
        'practitioner': '',
        'patient': '',
        'answers': [
            {
                'question_id': '',
                'patient_answer': '',
            }, #...
        ]
    }



+----------------------+-----------------------------------+--------+----------+
| Property             | Description                       | Type   | Required |
+======================+===================================+========+==========+
| practice             | ID of the Practice                | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| practitioner         | ID of the Practitioner            | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| patient              | ID of the Patient                 | Integer|    X     |
+----------------------+-----------------------------------+--------+----------+
| answers              | A collection of Answers objects   | List   |    X     |
+----------------------+-----------------------------------+--------+----------+
| question_id          | ID of the Evaluation Question     | Integer|    X     |
+----------------------+-----------------------------------+--------+----------+
| patient_answer       | Patient's response to the question| String |    X     |
+----------------------+-----------------------------------+--------+----------+

Response
--------

.. code-block:: js

    {
        'request': {
            'practice': '',
            'practitioner': '',
            'patient': '',
            'answers': [
                {
                    'question_id': '',
                    'patient_answer': '',
                }, #...
            ]
        },
        'response': {
            'evaluation_uuid': '',
        },
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the Eval ID     | Object |
+----------------------+-----------------------------------+--------+
| evaluation_uuid      | A unique UUID for the evaulation  | String |
|                      | records                           |        |
+----------------------+-----------------------------------+--------+


Retrieve Evaluation details
===========================
This endpoint is used to retrieve all the details of an Evaluation.

.. note:: **GET** /api/v1/evaluations/<UUID>

Response
--------

.. code-block:: js

    {
        'request': {
            'evaluation_uuid': '',
        },
        'response': {
            'evaluation_uuid': '',
            'practice': '',
            'practitioner': '',
            'patient': '',
            'answers': [
                {
                    'question_id': '',
                    'patient_answer': '',
                }, #...
            ]
            'active': '',
        }
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| evaluation_uuid      | A unique UUID for the evaulation  | String |
|                      | records                           |        |
+----------------------+-----------------------------------+--------+
| practice             | ID of the Practice                | Integer|
+----------------------+-----------------------------------+--------+
| practitioner         | ID of the Practitioner            | Integer|
+----------------------+-----------------------------------+--------+
| patient              | ID of the Patient                 | Integer|
+----------------------+-----------------------------------+--------+
| answers              | A collection of Answers objects   | List   |
+----------------------+-----------------------------------+--------+
| question_id          | ID of the Evaluation Question     | Integer|
+----------------------+-----------------------------------+--------+
| patient_answer       | Patient's response to the question| String |
+----------------------+-----------------------------------+--------+

Update an Evaluation
====================
This endpoint is used to update an evaluation in the Cagenix API. You must
resubmit all answer objects again.  So if an evaulation had 20 questions, all of
those answers must be resubmitted for an update.

.. note:: **PUT** /api/v1/evaluations/<uuid>

Call
----

.. code-block:: js

    {
        'evaluation_uuid': '',
        'practice': '',
        'practitioner': '',
        'patient': '',
        'answers': [
            {
                'question_id': '',
                'patient_answer': '',
            }, #...
        ]
        'active': '',
    }


+----------------------+-----------------------------------+--------+----------+
| Property             | Description                       | Type   | Required |
+======================+===================================+========+==========+
| evaluation_uuid      | A unique UUID for the evaulation  | String |    X     |
|                      | records                           |        |          |
+----------------------+-----------------------------------+--------+----------+
| practice             | ID of the Practice                | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| practitioner         | ID of the Practitioner            | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| patient              | ID of the Patient                 | Integer|          |
+----------------------+-----------------------------------+--------+----------+
| answers              | A collection of Answers objects   | List   |    X     |
+----------------------+-----------------------------------+--------+----------+
| question_id          | ID of the Evaluation Question     | Integer|    X     |
+----------------------+-----------------------------------+--------+----------+
| patient_answer       | Patient's response to the question| String |    X     |
+----------------------+-----------------------------------+--------+----------+

Response
--------

.. code-block:: js

    {
        'request': {
            'evaluation_uuid': '',
            'practice': '',
            'practitioner': '',
            'patient': '',
            'answers': [
                {
                    'question_id': '',
                    'patient_answer': '',
                }, #...
            ]
            'active': '',
        },
        'response': {
            'evaluation_uuid': '',
            'status': '',
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
| evaluation_uuid      | A unique UUID for the evaulation  | String |
|                      | records                           |        |
+----------------------+-----------------------------------+--------+
| status               | The result of the PUT opperation  | String |
|                      | (EX: Success, Failed)             |        |
+----------------------+-----------------------------------+--------+
| active               | Active Flag for Archiving         | Boolean|
+----------------------+-----------------------------------+--------+

Delete a patient
================
This endpoint is used to delete an evaluation in the Cagenix API.

.. note:: **DELETE** /api/v1/evaluations/<uuid>

Response
--------

.. code-block:: js

    {
        'request': {
            'evaluation_uuid': '',
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
| response             | Object containing the Evaluation  | Object |
|                      | UUID                              |        |
+----------------------+-----------------------------------+--------+
| status               | The result of the DELETE          | String |
|                      | opperation (EX: Success, Failed)  |        |
+----------------------+-----------------------------------+--------+
