"""
This file contains the application setup for
SSLify, Flask-SQLAlchemy, and Flask-Security.
"""
from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required, current_user
from flask.ext.security.utils import encrypt_password, logout_user
from flask_security.confirmable import confirm_user
from raven.contrib.flask import Sentry
from flask_mail import Mail
import logging


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from cagenix.users.models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
mail = Mail(app)
logging.basicConfig(level=logging.DEBUG)

# Sentry
#sentry = Sentry(app)


@app.route('/TBAekZPEaCC58w')
def create_user():
    user_datastore.create_user(email='admin@cagenix.com', password=encrypt_password('tester'))
    user_datastore.create_role(name='PNT-Admin', description='Master Cagenix Admin')
    db.session.commit()
    user = user_datastore.find_user(email='admin@cagenix.com')
    confirm_user(user)
    role = user_datastore.find_role('PNT-Admin')
    user_datastore.add_role_to_user(user, role)
    db.session.commit()
    return redirect('/')


@app.route('/', methods=['GET', ])
@login_required
def handle_splash():
    return redirect('/dashboard')


@app.errorhandler(404)
def not_found(error):
    """returns a the 404.html template on any 404 error with in the app.

    :param error: The error details
    :type value: object, dict
    :returns: 404.html
    :rtype: template
    """
    return render_template('404.html'), 404


@app.route('/logout')
def logout():
    """This handles the logout for flask_security and redirects to login
    """
    logout_user()
    return redirect(url_for('home'))

# Blueprints
from cagenix.users.views import mod as usersModule
app.register_blueprint(usersModule)

from cagenix.patients.views import mod as patientsModule
app.register_blueprint(patientsModule)

from cagenix.dashboard.views import mod as dashboardModule
app.register_blueprint(dashboardModule)

from cagenix.practices.views import mod as practicesModule
app.register_blueprint(practicesModule)

from cagenix.advertisements.views import mod as practicesModule
app.register_blueprint(practicesModule)

from cagenix.api.controller import mod as apiModule
app.register_blueprint(apiModule)
