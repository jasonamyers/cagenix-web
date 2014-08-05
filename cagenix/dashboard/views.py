"""cagenix.dashboard.views

This file defines the URL routes and controller logic for the dashboard blueprint.
PNT-Admins and App-Admins are the only uses that can access this blueprint.
"""

import logging
from flask import Blueprint, render_template, redirect, url_for, abort
from flask.ext.security import current_user
from flask.ext.security.decorators import roles_accepted
from cagenix import db

log = logging.getLogger(__name__)
mod = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@mod.route('', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def dashboard_home():
    return render_template('dashboard/index.html')
