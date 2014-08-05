"""cagenix.practices.models

This file is used to define all the models used by the Practices blueprint
"""

from cagenix import db


class Practice(db.Model):
    """The Practice model defines the authentication users used by Flask-Security

    :param db.Model: The SQLAlchemy base database model
    :type db.Model: object
    """
    __tablename__ = 'cagenix_practice'
    id = db.Column(db.Integer, primary_key=True)
    practice_name = db.Column(db.String(255))
    address_one = db.Column(db.String(255))
    address_two = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip_code = db.Column(db.String(10))
    url = db.Column(db.String(255))
    primary_color = db.Column(db.String(255))
    secondary_color = db.Column(db.String(255))
    phone = db.Column(db.String(12))
    active = db.Column(db.Boolean())
    practioneers = db.relationship('User', backref='practice', lazy='dynamic')
    patients = db.relationship('Patient', backref='practice', lazy='dynamic')

    def __repr__(self):
        """__repr__ specifies what a role looks like when viewed in the shell

        :param self: A Practice Instance
        :type cls: class
        """
        return '<practice %r>' % (self.practice_name)

    @classmethod
    def by_id(cls, practice_id):
        """by_id returns a User object given a user_id

        :param cls: The calling class
        :type cls: class
        :param user_id: The id of the user being searched for
        :type user_id: int
        """
        return db.session.query(Practice).filter(Practice.id == practice_id).first()

    @classmethod
    def by_phone(cls, phone):
        """by_phone returns a User object given a phone number

        :param cls: The calling class
        :type cls: class
        :param phone: The phone number of the user being searched for
        :type phone: string
        """

    @classmethod
    def get_practices(cls):
        """get_practices returns a list of Practice objects

        :param cls: The calling class
        :type cls: class
        """
        return db.session.query(Practice).order_by(Practice.practice_name)
