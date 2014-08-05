"""cagenix.advertisements.views

This file defines the URL routes and controller logic for the patients blueprint.
"""

import logging

from flask import Blueprint, render_template, redirect, url_for, abort
from flask import current_app as app
from flask.ext.security.decorators import roles_accepted

from cagenix import db
from cagenix.advertisements.models import Advertisement
from cagenix.advertisements.forms import AdvertisementCreateForm
from cagenix.advertisements.file_handler import s3_upload

log = logging.getLogger(__name__)
mod = Blueprint('advertisements', __name__, url_prefix='/advertisements')


@mod.route('', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def home():
    """This function handles the /users endpoint for the blueprint

    It displays a list of users and their roles with the ability to edit or
    change passwords. It also displays a list of roles and descriptions with
    the ability to edit them.  It also offers the ability to add additional
    users and roles.

    :returns: users/index.html
    :rtype: template
    """
    ads = db.session.query(Advertisement).all()
    advertisements = []
    for ad in ads:
        advertisements.append(
            {
                'name': ad.name,
                'position': ad.position,
                'active': ad.active,
                'asset_location': app.config['AWS_LOCATION'] + app.config['AWS_DIRECTORY'] + '/' + ad.asset_location,
                'ad_id': ad.id,
            }
        )

    return render_template('advertisements/index.html', advertisements=advertisements)


@mod.route('/create', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin', 'App-Admin')
def advertisements_create():
    """This function handles the /users/create endpoint for the blueprint

    It allows PNT-Admins to create users.  It uses the :ref:`users-forms-label`
    to display UsersCreateForm

    :returns: users/index.html
    :rtype: template
    """
    ad = Advertisement()
    form = AdvertisementCreateForm()
    if form.validate_on_submit():
        form.populate_obj(ad)
        ad.asset_location = s3_upload(form.ad_file)
        db.session.add(ad)
        db.session.commit()
        return redirect(url_for('advertisements.home'))
    return render_template('advertisements/create.html', form=form, admin=True)


@mod.route('/delete/<ad_id>', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def advertisements_delete(ad_id):
    """This function handles the /users/create endpoint for the blueprint

    It allows PNT-Admins to create users.  It uses the :ref:`users-forms-label`
    to display UsersCreateForm

    :returns: users/index.html
    :rtype: template
    """
    ad = Advertisement.by_id(ad_id)
    db.session.delete(ad)
    db.session.commit()

    return redirect(url_for('advertisements.home'))
