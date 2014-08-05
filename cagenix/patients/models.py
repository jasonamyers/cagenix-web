"""cagenix.users.models

This file is used to define all the models used by the Users blueprint
"""

from cagenix import db


class Patient(db.Model):
    """The User model defines the authentication users used by Flask-Security

    This Role class defines the model attributes, a classmethod to make finding
    the users easier. It also contains several fields unexposed by the UI. Those
    fields are used to track user logins and access IPs.

    :param db.Model: The SQLAlchemy base database model
    :type db.Model: object
    :param UserMixin: The UserMixin base provided by Flask-Security
    :type UserMixin: object
    """
    __tablename__ = 'cagenix_patient'
    id = db.Column(db.Integer, primary_key=True)
    dentist_id = db.Column(db.Integer, db.ForeignKey('cagenix_user.id'), nullable=True)
    practice_id = db.Column(db.Integer, db.ForeignKey('cagenix_practice.id'), nullable=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address_one = db.Column(db.String(255))
    address_two = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip_code = db.Column(db.String(10))
    email = db.Column(db.String(255), unique=True)
    active = db.Column(db.Boolean(), default=True)
    choice_one = db.Column(db.String(255))
    choice_two = db.Column(db.String(255))
    choice_three = db.Column(db.String(255))

    #def __init__(self, first_name=None, last_name=None):
        #"""__init__ initializes a User object given a some info

        #:param self: A User Instance
        #:type cls: class
        #:param username: The username of the User being initialized
        #:type username: string
        #:param password: The password of the User being initialized
        #:type password: string
        #"""
        #self.first_name = first_name
        #self.last_name = last_name

    def __repr__(self):
        """__repr__ specifies what a role looks like when viewed in the shell

        :param self: A Role Instance
        :type cls: class
        """
        return '<Patient %r %r>' % (self.first_name, self.last_name)

    def map_data(self, data):
        ''' map_data takes a dict as an argument. It then iterates
        over each key field in the fields list, if a key is
        in the supplied dict, it will then update the attribute of
        this object to reflect the value of that key in the dict.
        '''

        fields = [
            'first_name', 'last_name', 'address_one', 'address_two', 'city',
            'state', 'zip_code', 'email', 'active', 'choice_one', 'choice_two',
            'choice_three', 'practice_id', 'dentist_id'
        ]

        for field in fields:
            if field in data:
                setattr(self, field, data.get(field))

    @classmethod
    def by_id(cls, user_id):
        """by_id returns a User object given a user_id

        :param cls: The calling class
        :type cls: class
        :param user_id: The id of the user being searched for
        :type user_id: int
        """
        return db.session.query(Patient).filter(Patient.id == user_id).first()

    @classmethod
    def by_phone(cls, phone):
        """by_phone returns a User object given a phone number

        :param cls: The calling class
        :type cls: class
        :param phone: The phone number of the user being searched for
        :type phone: string
        """
        return db.session.query(Patient).filter(Patient.phone == phone).first()

    @classmethod
    def by_email(cls, email):
        """by_email returns a User object given an email address.

        :param cls: The calling class
        :type cls: class
        :param email: The email of the user being searched for
        :type email: string
        """
        return db.session.query(Patient).filter(Patient.email == email).first()
