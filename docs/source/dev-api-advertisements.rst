##################
Advertisements API
##################


Retrieve Advertisement details
==============================
This endpoint is used to retrieve most details of an Advertisement.

.. note:: **GET** /api/v1/advertisements

Response
--------

.. code-block:: js

    {
        'request': {
        },
        'response': {
            'advertisements': [
                {
                    'id': '',
                    'name': '',
                    'asset_location': '',
                    'position': '',
                    'position': '',
                } #...
            ]
        }
    }

+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| advertisements       | A collection of Ad objects        | List   |
+----------------------+-----------------------------------+--------+
| id                   | ID of the Advertisement           | String |
+----------------------+-----------------------------------+--------+
| name                 | Banner Name                       | String |
+----------------------+-----------------------------------+--------+
| asset_location       | Location of asset or resource name| String |
+----------------------+-----------------------------------+--------+
| position             | Screen Position                   | String |
+----------------------+-----------------------------------+--------+


Retrieve Advertisement details
==============================
This endpoint is used to retrieve most details of an Advertisement.

.. note:: **GET** /api/v1/advertisements/<ID>

Response
--------

.. code-block:: js

    {
        'request': {
            'advertisement_id': '',
        },
        'response': {
            'name': '',
            'asset_location': '',
            'position': '',
            'active': '',
        }
    }

+----------------------+-----------------------------------+--------+
| Property             | Description                       | Type   |
+======================+===================================+========+
| name                 | Banner Name                       | String |
+----------------------+-----------------------------------+--------+
| asset_location       | Location of asset or resource name| String |
+----------------------+-----------------------------------+--------+
| position             | Screen Position                   | String |
+----------------------+-----------------------------------+--------+
| active               | Active Flag for Archiving         | String |
+----------------------+-----------------------------------+--------+
