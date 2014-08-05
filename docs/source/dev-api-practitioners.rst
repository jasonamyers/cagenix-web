#################
Practitioners API
#################


Create a Practitioner
=====================
This endpoint is used to create a practitioner in the Cagenix API.

.. note:: **POST** /api/v1/practitioners/create

** This endpoint is open, and only requires the following headers:**

.. code-block:: js

    {
        'content-type': 'application/json'
    }


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
        'password': '',
        'activation_code': '',
        'primary_color': '',
        'secondary_color': '',
        'practice': '',
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
| email                | Email address                     | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| password             | Password                          | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| activation_code      | Code used for initial account     | String |    X     |
|                      | setup                             |        |          |
+----------------------+-----------------------------------+--------+----------+
| primary_color        | Primary Branding Color            | String |          |
+----------------------+-----------------------------------+--------+----------+
| secondary_color      | Secondary Branding Color          | String |          |
+----------------------+-----------------------------------+--------+----------+
| practice             | ID of the Practice                | Integer|          |
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
            'password': 'XXX',
            'activation_code': '',
            'primary_color': '',
            'secondary_color': '',
            'practice': '',
        },
        'response': {
            'practitioner_id': '',
        },
    }

+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the Practitioner| Object |
|                      | ID                                |        |
+----------------------+-----------------------------------+--------+
| practitioner_id      | A unique ID for the Partitioner   | Integer|
|                      | record                            |        |
+----------------------+-----------------------------------+--------+

Retrieve Practitioner details
=============================
This endpoint is used to retrieve most details of a Practitioner.

.. note:: **GET** /api/v1/practitioners/<ID>

Response
--------

.. code-block:: js

    {
        'request': {
            'practitioner_id': '',
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
            'activation_code': '',
            'primary_color': '',
            'secondary_color': '',
            'practice': '',
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
| activation_code      | Code used for initial account     | String |
|                      | setup                             |        |
+----------------------+-----------------------------------+--------+
| primary_color        | Primary Branding Color            | String |
+----------------------+-----------------------------------+--------+
| secondary_color      | Secondary Branding Color          | String |
+----------------------+-----------------------------------+--------+
| practice             | ID of the Practice                | Integer|
+----------------------+-----------------------------------+--------+

Update a Practitioner
=====================
This endpoint is used to update a practitioner in the Cagenix API.

.. note:: **PUT** /api/v1/practitioners/<id>

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
        'primary_color': '',
        'secondary_color': '',
        'practice': '',
    }


+----------------------+-----------------------------------+--------+----------+
| Property             | Description                       | Type   | Required |
+======================+===================================+========+==========+
| active               | Active Flag for Archiving         | Boolean|          |
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
| primary_color        | Primary Branding Color            | String |          |
+----------------------+-----------------------------------+--------+----------+
| secondary_color      | Secondary Branding Color          | String |          |
+----------------------+-----------------------------------+--------+----------+
| practice             | ID of the Practice                | Integer|          |
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
            'active': '',
            'primary_color': '',
            'secondary_color': '',
            'practice': '',
        },
        'response': {
            'practitioner_id': '',
            'active': '',
        },
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the Practitioner| Object |
|                      | ID                                |        |
+----------------------+-----------------------------------+--------+
| practitioner_id      | A unique ID for the Partitioner   | Integer|
|                      | record                            |        |
+----------------------+-----------------------------------+--------+
| active               | Active Flag for Archiving         | Boolean|
+----------------------+-----------------------------------+--------+

Delete a Practitioner
=====================
This endpoint is used to Delete a practitioner in the Cagenix API.

.. note:: **DELETE** /api/v1/practitioners/<id>

Response
--------

.. code-block:: js

    {
        'request': {
            'practitioner_id': '',
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
| response             | Object containing the Practitioner| Object |
|                      | ID                                |        |
+----------------------+-----------------------------------+--------+
| status               | The result of the DELETE          | String |
|                      | opperation (EX: Success, Failed)  |        |
+----------------------+-----------------------------------+--------+

Authenticate a Practitioner
===========================
This endpoint is used to get the secret key for a practitioner in the Cagenix API.
This POST request will be made over SSL and will be protected from outside
attack via that encryption.

.. note:: **POST** /api/v1/practitioners/login

** This endpoint is open, and only requires the following headers:**

.. code-block:: js

    {
        'content-type': 'application/json'
    }


Call
----

.. code-block:: js

    {
        'email': '',
        'password': '',
    }


+----------------------+-----------------------------------+--------+----------+
| Property             | Description                       | Type   | Required |
+======================+===================================+========+==========+
| email                | email address                     | String |    X     |
+----------------------+-----------------------------------+--------+----------+
| password             | Password                          | String |    X     |
+----------------------+-----------------------------------+--------+----------+

Response
--------

.. code-block:: js

    {
        'request': {
            'email': '',
        },
        'response': {
            'secret': '',
        },
    }


+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| request              | Object containing the original    | Object |
|                      | request data                      |        |
+----------------------+-----------------------------------+--------+
| response             | Object containing the secret for  | Object |
|                      | API access                        |        |
+----------------------+-----------------------------------+--------+
| secret               | The secret for API Access         | String |
+----------------------+-----------------------------------+--------+
