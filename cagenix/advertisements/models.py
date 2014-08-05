"""cagenix.advertisements.models

This file is used to define all the models used by the Advertisement blueprint
"""

from cagenix import db


class Advertisement(db.Model):
    """The User model defines the authentication users used by Flask-Security

    This Role class defines the model attributes, a classmethod to make finding
    the users easier. It also contains several fields unexposed by the UI. Those
    fields are used to track user logins and access IPs.

    :param db.Model: The SQLAlchemy base database model
    :type db.Model: object
    :param UserMixin: The UserMixin base provided by Flask-Security
    :type UserMixin: object
    """
    __tablename__ = 'cagenix_advertisement'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    asset_location = db.Column(db.String(255))
    position = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    counter = db.Column(db.Integer)

    def __repr__(self):
        """__repr__ specifies what a role looks like when viewed in the shell

        :param self: A Role Instance
        :type cls: class
        """
        return '<Ad %r >' % (self.name)

    @classmethod
    def by_id(cls, advertisement_id):
        """by_id returns a User object given a user_id

        :param cls: The calling class
        :type cls: class
        :param advertisement_id: The id of the advertisement being searched for
        :type advertisement_id: int
        """
        return db.session.query(Advertisement).filter(Advertisement.id == advertisement_id).first()
