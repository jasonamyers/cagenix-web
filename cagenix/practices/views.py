"""cagenix.patients.views

This file defines the URL routes and controller logic for the patients blueprint.
"""

import logging
from flask import Blueprint, render_template, redirect, url_for

from flask.ext.security.decorators import roles_accepted
from cagenix import db

from .models import Practice
from .forms import PracticeCreateForm

log = logging.getLogger(__name__)
mod = Blueprint('practices', __name__, url_prefix='/practices')


@mod.route('', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def home():
    practices = Practice.query.all()
    return render_template('practices/index.html', practices=practices)


@mod.route('/create', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin', 'App-Admin')
def practices_create():
    """This function handles the /practices/create endpoint for the blueprint

    It allows Admins to create Practices.  It uses the :ref:`practices-forms-label`
    to display PracticesCreateForm

    :returns: practices/create.html
    :rtype: template
    """
    practice = Practice()
    form = PracticeCreateForm()
    if form.validate_on_submit():

        form.populate_obj(practice)
        db.session.add(practice)
        db.session.commit()
        return redirect(url_for('practices.home'))
    return render_template('practices/create.html', form=form)


@mod.route('/delete/<practice_id>', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def practices_delete(practice_id):
    """This function handles the /users/create endpoint for the blueprint

    It allows PNT-Admins to create users.  It uses the :ref:`users-forms-label`
    to display UsersCreateForm

    :returns: users/index.html
    :rtype: template
    """
    practice = Practice.by_id(practice_id)
    db.session.delete(practice)
    db.session.commit()

    return redirect(url_for('practices.home'))
