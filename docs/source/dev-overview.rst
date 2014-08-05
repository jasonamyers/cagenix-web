##################
Developer Overview
##################

The following document covers the internals of the Cagenix-Web
application.  Below is a list of libraries used in the application,
and the general application settings.

Libraries
---------
* Flask - Web Framework `Documentation <http://flask.pocoo.org/>`_
* Flask-SQLAlchemy - Simplifies the usage of SQLAlchemy within the Flask framework.
  Check out the `Road to Enlightenment <http://packages.python.org/Flask-SQLAlchemy/quickstart.html#road-to-enlightenment>`_
  for more details.  `SQLAlchemy Docs <http://docs.sqlalchemy.org/en/rel_0_8/>`_
* WTForms - Provides a flexible way of handling forms `Documentation <(http://wtforms.simplecodes.com/docs/1.0.3/>`_
* Flask-WTF - Provides a simple integration with WTForms `Documentation <(http://packages.python.org/Flask-WTF/>`_
* Jinja2 - The prefered templating language for Flask `Documentation <http://jinja.pocoo.org/docs/>`_
* Flask-Security - A very powerful collection of User Authentication/Authorization/Accounting
  `Documentation <http://flask-security.readthedocs.org/en/latest/index.html>`_
* Passlib - A stong password hashing utility `Documentation <http://packages.python.org/passlib/new_app_quickstart.html#pbkdf2>`_
* Unicodecsv - Used to handle csv files that contain unicode characters `Documentation <https://github.com/jdunck/python-unicodecsv>`_

It's built using the `Flask Large App How To <https://github.com/mitsuhiko/flask/wiki/Large-app-how-to)>`_ and `Matt Wright's Guide <http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html?utm_medium=referral&utm_source=pulsenews#s2c>`_

General Application Setup (__init__.py)
------------------------------------------

.. automodule:: cagenix
    :members:
    :undoc-members:
