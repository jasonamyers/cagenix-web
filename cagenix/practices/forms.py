"""cagenix.practices.forms

This file is used to define all the WTForms used by the Practices blueprint
"""
from flask_wtf import Form
from wtforms import TextField, validators, HiddenField, BooleanField


strip_filter = lambda x: x.strip() if x else None


class PracticeCreateForm(Form):
    """This form is used by Admin roles to create new Practices

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    practice_name = TextField('Practice Name', [validators.Length(min=1, max=255)], filters=[strip_filter])
    address_one = TextField('Address One', [validators.Length(min=1, max=255)], filters=[strip_filter])
    address_two = TextField('Address Two', [], filters=[strip_filter])
    city = TextField('City', [validators.Length(min=1, max=255)], filters=[strip_filter])
    state = TextField('State', [validators.Length(min=1, max=255)], filters=[strip_filter])
    zip_code = TextField('ZIP Code', [validators.Length(min=1, max=255)], filters=[strip_filter])
    url = TextField('Website Address', [validators.Length(min=1, max=255)], filters=[strip_filter])
    phone = TextField('Phone Number', [validators.Length(min=1, max=255)], filters=[strip_filter])


class PracticeEditForm(PracticeCreateForm):
    """This form is used by Admin roles to edit Practices

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    id = HiddenField()
    active = BooleanField('Active', [validators.Length(min=1, max=255)], filters=[strip_filter])
