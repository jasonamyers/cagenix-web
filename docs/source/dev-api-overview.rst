############
API Overview
############
The following document will walk you through using the Cagenix API
within your application.

Base URL, HTTPS, and Versioning
===============================

Base URI
--------
The Cagenix API root is located at:
https://cagenix-web.herokuapp.com/api/v1/

HTTP and HTTPS
--------------
The Cagenix API is served over HTTP and HTTPS during testing. The final
deployment will be HTTPS only, prefer to testing that method.

Versioning
----------
Currently the Cagenix API does not require any type of versioning in the
requests as it is in the URI.

Message Body
------------
When submitting a request to the Cagenix API with a message body, the
variables within that body should be UTF8 encoded and within a JSON object.

Credentials
===========
In order to access the Cagenix API each developer/user must request a key and
a secret from the application admins. These two keys will be used in the
following formulas which will provide the properly formatted header values
required for all POST, PUT, PATCH, and DELETE requests. All GET requests require
the key, timestamp, and signature url parameters.

GET Requests
============
A properly formed GET request includes the email, timestamp, and signature url
parameters. The email is the email provided by the application admins.  The
signature is made of the hmac digest of the SECRET, QueryString(email and timestamp) encoded to
UTF8 hashed via sha512 and base 64 encoded.


+------------------+-----------------------------------------------------------+
| URL Param        | Description                                               |
+==================+===========================================================+
| email            | The Practitioners/Users email address                     |
+------------------+-----------------------------------------------------------+
| timestamp        | This is the date and time, ISO format, used in your       |
|                  | header formulas. An example is 2012-10-29T01:30:20Z.      |
|                  | Notice the T and Z, with the T separating the date and    |
|                  | time and Z ending the string.                             |
+------------------+-----------------------------------------------------------+
| signature        | The header signature is a string that combines the body   |
|                  | hash, date and time, along with your secret, encoded to   |
|                  | UTF8 and hashed using sha256.                             |
+------------------+-----------------------------------------------------------+

.. note:: Signature = Base64( hmac_digest( Secret, UTF-8-Encoding-Of( QueryString ), sha512 ) ) ) )

Signature Example

::

    Base64( hmac_digest( secret, UTF-8-Encoding-Of('email=jason%40mailthemyers.com&timestamp=2014-02-01T03%3A49%3A38.000Z'), sha512 ) ) ) )
    would result in
    qs81oYv+HsgF4s/2FHb/OBrs8Y3elMWIOweD+ZUUvroAkJsen1Mfo8UR72ywulMCUwRLKPUwZj2qcMAc6tQpiA==


    This assumes:
        email is jason@mailthemyers.com
        Secret is cf741fa70d20938f003677a24d73cbcb
        Time is 3:39:38 on 2/01/2014

URL Example

::

    /api/v1/practitioners/2?code=qs81oYv+HsgF4s/2FHb/OBrs8Y3elMWIOweD+ZUUvroAkJsen1Mfo8UR72ywulMCUwRLKPUwZj2qcMAc6tQpiA==&email=jason%40mailthemyers.com&timestamp=2014-02-01T03%3A49%3A38.000Z

    This assumes:
        email is jason@mailthemyers.com
        Secret is cf741fa70d20938f003677a24d73cbcb
        Time is 3:39:38 on 2/01/2014


Headers
=======
When interacting with the Cagenix web-service, the following headers are
required to be submitted with each request.

+------------------+-----------------------------------------------------------+
| Header Element   | Description                                               |
+==================+===========================================================+
| Content-Type     | application/json                                          |
|                  | Currently XML and other formats are not available.        |
+------------------+-----------------------------------------------------------+
| email            | The Practitioners/Users email address                     |
+------------------+-----------------------------------------------------------+
| datetime         | This is the date and time, ISO format, used in your       |
|                  | header formulas. An example is 2012-10-29T01:30:20Z.      |
|                  | Notice the T and Z, with the T separating the date and    |
|                  | time and Z ending the string.                             |
+------------------+-----------------------------------------------------------+
| body_hash        | This is the encoding of the body contents through the     |
|                  | following formula. If there are no body contents to be    |
|                  | sent, encode and send an empty body array.                |
+------------------+-----------------------------------------------------------+
| signature        | The header signature is a string that combines the body   |
|                  | hash, date and time, along with your secret, encoded to   |
|                  | UTF8 and hashed using sha256.                             |
+------------------+-----------------------------------------------------------+
| lang             | The language of the request content. Example is 'en'.     |
+------------------+-----------------------------------------------------------+

Header Formulas
===============

+------------------+-----------------------------------------------------------+
| Header Element   | Formula                                                   |
+==================+===========================================================+
| datetime         | The date and time is a simple formatting:                 |
|                  | yyyy-mm-ddThh:mm:ssZ                                      |
+------------------+-----------------------------------------------------------+
| body_hash        | json body content UTF8 encoded, then sha256 hashed.       |
+------------------+-----------------------------------------------------------+
| signature        | body_hash added to datetime added to secret key, encoded  |
|                  | to UTF8 then sha256 hashed.                               |
+------------------+-----------------------------------------------------------+

Response Codes
==============

GET Request Response Codes
--------------------------

+------+---------------------+-------------------------------------------------+
| CODE | Response            | Meaning                                         |
+======+=====================+=================================================+
| 200  | OK                  | The request was successful and the body contains|
|      |                     | what you asked for.                             |
+------+---------------------+-------------------------------------------------+
| 401  | Unauthorized        | Your credentials do not authorize you to access |
|      |                     | the requested info.                             |
+------+---------------------+-------------------------------------------------+
| 404  | Not Found           | The service you requested was not found on our  |
|      |                     | server.                                         |
+------+---------------------+-------------------------------------------------+
| 500  | Server Error        | There was an internal error, if it continues,   |
|      |                     | please contact us.                              |
+------+---------------------+-------------------------------------------------+
| 503  | Service Unavailable | The service requested is temporarily down. Try  |
|      |                     | again later.                                    |
+------+---------------------+-------------------------------------------------+

POST/PUT Request Response Codes
-------------------------------

+------+---------------------+-------------------------------------------------+
| CODE | Response            | Meaning                                         |
+======+=====================+=================================================+
| 200  | OK                  | The request was successful and the body contains|
|      |                     | what you asked for.                             |
+------+---------------------+-------------------------------------------------+
| 201  | Created             | The resource you requested by create was        |
|      |                     | successfully created.                           |
+------+---------------------+-------------------------------------------------+
| 400  | Bad Request         | Something was wrong in your request, check the  |
|      |                     | message for details.                            |
+------+---------------------+-------------------------------------------------+
| 401  | Unauthorized        | Your credentials do not authorize you to access |
|      |                     | the requested info.                             |
+------+---------------------+-------------------------------------------------+
| 404  | Not Found           | The service you requested was not found on our  |
|      |                     | server.                                         |
+------+---------------------+-------------------------------------------------+
| 405  | Method Not Allowed  | You tried POSTing or PUTting to a service that  |
|      |                     | can’t accept data.                              |
+------+---------------------+-------------------------------------------------+
| 500  | Server Error        | There was an internal error, if it continues,   |
|      |                     | please contact us.                              |
+------+---------------------+-------------------------------------------------+

DELETE Request Response Codes
-----------------------------

+------+---------------------+-------------------------------------------------+
| CODE | Response            | Meaning                                         |
+======+=====================+=================================================+
| 204  | OK                  | The request was successfully deleted.           |
+------+---------------------+-------------------------------------------------+
| 400  | Bad Request         | Something was wrong in your request, check the  |
|      |                     | message for details.                            |
+------+---------------------+-------------------------------------------------+
| 401  | Unauthorized        | Your credentials do not authorize you to access |
|      |                     | the requested info.                             |
+------+---------------------+-------------------------------------------------+
| 404  | Not Found           | The service you requested was not found on our  |
|      |                     | server.                                         |
+------+---------------------+-------------------------------------------------+
| 405  | Method Not Allowed  | You tried POSTing or PUTting to a service that  |
|      |                     | can’t accept data.                              |
+------+---------------------+-------------------------------------------------+
| 500  | Server Error        | There was an internal error, if it continues,   |
|      |                     | please contact us.                              |
+------+---------------------+-------------------------------------------------+

