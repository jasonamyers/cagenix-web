"""cagenix.advertisements.forms

This file is used to define all the WTForms used by the Advertisements blueprint
"""
from flask_wtf import Form
from flask_wtf.file import FileField

from wtforms import TextField, validators, HiddenField, BooleanField


strip_filter = lambda x: x.strip() if x else None


class AdvertisementCreateForm(Form):
    """This form is used by Admin roles to create new Practices

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    name = TextField('Ad Name', [validators.Length(min=1, max=255)], filters=[strip_filter])
    position = TextField('Ad Position', [validators.Length(min=1, max=255)], filters=[strip_filter])
    ad_file = FileField('Ad File')


class AdvertisementEditForm(AdvertisementCreateForm):
    """This form is used by Admin roles to edit Advertisements

    :param Form: The WTForms base class
    :type value: object
    :returns: WTForm
    :rtype: object
    """
    id = HiddenField()
    active = BooleanField('Active', [validators.Length(min=1, max=255)], filters=[strip_filter])
