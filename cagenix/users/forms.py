"""cornerstone.users.forms

This file is used to define all the WTForms used by the Users blueprint
"""
from flask_wtf import Form
from wtforms import TextField, validators, HiddenField, PasswordField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from flask.ext.security import current_user
from cagenix.users.models import Role
from cagenix.practices.models import Practice


strip_filter = lambda x: x.strip() if x else None


class UserCreateForm(Form):
    """This form is used by CS-Admin roles to create new users

    Users require an email and a password. This form uses a QuerySelectField to
    produce a list of Merchants that can optionally be associationed to a user.
    A QuerySelectMulipleField for Roles can also optionally be associated with
    a client. A client can have as many roles as needed.

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    email = TextField('Email Address', [validators.Email()], filters=[strip_filter])
    first_name = TextField('First Name', [validators.Length(min=1, max=255)], filters=[strip_filter])
    last_name = TextField('Last Name', [validators.Length(min=1, max=255)], filters=[strip_filter])
    practice = QuerySelectField(get_pk=lambda x: x.id, get_label='practice_name', query_factory=Practice.get_practices, allow_blank=True, blank_text=u'')
    roles = QuerySelectMultipleField(get_label='name', query_factory=Role.get_roles, allow_blank=True, blank_text=u'')


class UserEditForm(Form):
    """This form is used by CS-Admin roles to edit users

    Admins can change the email, active state of the user, associated Merchants,
    and assigned Roles. This form uses a QuerySelectField to produce a list of
    Merchants that can optionally be associationed to a user. A
    QuerySelectMulipleField for Roles can also optionally be associated with
    a client. A client can have as many roles as needed.

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    id = HiddenField()
    email = TextField('Email Address', [validators.Email()], filters=[strip_filter])
    #merchant = QuerySelectField(get_pk=lambda x: x.merchant_id, get_label='company_name', query_factory=Merchants.get_merchants, allow_blank=True, blank_text=u'')
    roles = QuerySelectMultipleField(get_label='name', query_factory=Role.get_roles, allow_blank=True, blank_text=u'')
    active = BooleanField('Active')


class UserChangePasswordForm(UserCreateForm):
    """This form is used by CS-Admin roles to change a users password

    This form is used due to the handling of the change password process by
    Flask-Security.

    :param UserCreateForm: The same form used by the Create User process
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    pass


class RoleCreateForm(Form):
    """This form is used by CS-Admin roles to create a new role

    This form is used to create new roles with a name and description.

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    name = TextField('Role Name', [validators.Length(min=1, max=255)],
        filters=[strip_filter])
    description = TextField('Description', [validators.Length(min=1, max=255)],
        filters=[strip_filter])


class RoleEditForm(RoleCreateForm):
    """This form is used by CS-Admin roles to edit a role

    This form is used to change the name or description of a role.

    :param RoleCreateForm: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    id = HiddenField()
