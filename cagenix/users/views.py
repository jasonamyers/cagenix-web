"""cagenix.users.views

This file defines the URL routes and controller logic for the users blueprint.
PNT-Admins and App-Admins are the only uses that can access this blueprint.
The Flask-Security roles_accepted decorator is used to require both
authentication and authorization.
"""
import random
import logging
from flask import Blueprint, render_template, redirect, url_for, abort, request
from flask.ext.security import current_user
from flask.ext.security.utils import encrypt_password
from flask.ext.security.decorators import roles_accepted
from flask_mail import Message
from cagenix import db, mail
from cagenix.users.models import User, Role
from cagenix.users.forms import (UserCreateForm, UserEditForm,
    UserChangePasswordForm, RoleCreateForm, RoleEditForm)

log = logging.getLogger(__name__)
mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def users_home():
    """This function handles the /users endpoint for the blueprint

    It displays a list of users and their roles with the ability to edit or
    change passwords. It also displays a list of roles and descriptions with
    the ability to edit them.  It also offers the ability to add additional
    users and roles.

    :returns: users/index.html
    :rtype: template
    """
    roles = db.session.query(Role).all()
    users_query = db.session.query(User)
    if current_user.has_role('App-Admin'):
        users_query = users_query.filter(-User.roles.name.in_(['PNT-Admin']))
    users = users_query.outerjoin('roles').order_by(Role.name).all()
    return render_template('users/index.html', users=users, roles=roles)


@mod.route('/create', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin', 'App-Admin')
def users_create():
    """This function handles the /users/create endpoint for the blueprint

    It allows PNT-Admins to create users.  It uses the :ref:`users-forms-label`
    to display UsersCreateForm

    :returns: users/index.html
    :rtype: template
    """
    user = User()
    form = UserCreateForm()
    if form.validate_on_submit():
        form.populate_obj(user)
        user.activation_code = ''.join(random.sample('0123456789ABCDEFGHJKMNPQRTVWXYZ', 15))
        msg = Message("Welcome to Cagenix", recipients=[user.email])
        msg.body = "Welcome to the cagenix app, please use the code %(activation_code)s to activate the application" % {'activation_code': user.activation_code}
        mail.send(msg)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.users_home'))
    return render_template('users/create.html', form=form, admin=True)


@mod.route('/edit/<id>', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin', 'App-Admin')
def users_edit(id):
    """This function handles the /users/edit endpoint for the bcornerstone/users/views.py

    It allows PNT-Admins to edit users.  It uses the :ref:`users-forms-label`
    to display UsersEditForm

    :param id: The id of the user being edited
    :type id: int
    :returns: users/edit.html
    :rtype: template
    """
    user = User.by_id(id)
    if not user:
        abort(404)

    form = UserEditForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.users_home'))
    return render_template('users/edit.html', form=form, user_id=user.id, admin=True)


@mod.route('/changepassword/<id>', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin', 'App-Admin')
def users_changepassword(id):
    """This function handles the /users/changepassword endpoint for the blueprint

    It allows PNT-Admins to change a users password.  It uses the
    :ref:`users-forms-label` to display UsersChangePasswordForm

    :param id: The id of the user being edited
    :type id: int
    :returns: users/change_password.html
    :rtype: template
    """
    user = User.by_id(id)
    if not user:
        abort(404)

    form = UserChangePasswordForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        user.password = encrypt_password(user.password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.users_home'))
    return render_template('users/change_password.html', form=form, user_id=user.id, admin=True)


@mod.route('/delete/<id>', methods=['GET'])
@roles_accepted('PNT-Admin', 'App-Admin')
def users_delete(id):
    """This function handles the /users/delete endpoint for the blueprint

    It allows PNT-Admins to delete a user.  It is called via a button on
    the ``users/edit.html`` template

    :param id: The id of the user being deleted
    :type id: int
    :returns: users.users_home
    :rtype: redirect
    """
    user = User.by_id(id)
    if not user:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users.users_home'))


@mod.route('/roles/create', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin')
def roles_create():
    """This function handles the /users/roles/create endpoint for the blueprint

    It allows PNT-Admins to create roles.  It uses the :ref:`users-forms-label`
    to display RolesCreateForm

    :returns: users/roles/create.html
    :rtype: template
    """
    role = Role()
    form = RoleCreateForm()
    if form.validate_on_submit():
        form.populate_obj(role)
        db.session.add(role)
        db.session.commit()
        return redirect(url_for('users.users_home'))
    return render_template('users/roles/create.html', form=form, admin=True)


@mod.route('/roles/edit/<id>', methods=['GET', 'POST'])
@roles_accepted('PNT-Admin')
def roles_edit(id):
    """This function handles the /roles/edit endpoint for the blueprint

    It allows PNT-Admins to edit roles.  It uses the :ref:`users-forms-label`
    to display RolesEditForm

    :param id: The id of the role being edited
    :type id: int
    :returns: users/roles/edit.html
    :rtype: template
    """
    role = Role.by_id(id)
    if not role:
        abort(404)

    form = RoleEditForm(obj=role)
    if form.validate_on_submit():
        form.populate_obj(role)
        db.session.add(role)
        db.session.commit()
        return redirect(url_for('users.users_home'))
    return render_template('users/roles/edit.html', form=form, role_id=role.id, admin=True)


@mod.route('/roles/delete/<id>', methods=['GET'])
@roles_accepted('PNT-Admin')
def roles_delete():
    """This function handles the /users/roles/delete endpoint for the blueprint

    It allows PNT-Admins to delete a role.  It is called via a button on the
    ``users/roles/edit.html`` template

    :param id: The id of the role being edited
    :type id: int
    :returns: users.users_home
    :rtype: redirect
    """
    role = Role.by_id(id)
    if not role:
        abort(404)
    db.session.delete(role)
    db.session.commit()
    return redirect(url_for('users.users_home'))
