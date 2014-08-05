"""cagenix.patients.views

This file defines the URL routes and controller logic for the patients blueprint.
"""

import logging
from flask import Blueprint, render_template, redirect, url_for, abort
from cagenix import db

log = logging.getLogger(__name__)
mod = Blueprint('patients', __name__, url_prefix='/patients')
