"""cagenix.users.models

This file is used to define all the models used by the Users blueprint
"""
import datetime
import hashlib
import os

from flask.ext.security import UserMixin, RoleMixin

from cagenix import db
from cagenix.patients.models import Patient

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('cagenix_user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('cagenix_role.id')))


class Role(db.Model, RoleMixin):
    """The Role model defines the authorization roles used by Flask-Security

    This Role class defines the model attributes, and several classmethods to
    make using the class easier.

    :param db.Model: The SQLAlchemy base database model
    :type db.Model: object
    :param RoleMixin: The RoleMixin base provided by Flask-Security
    :type RoleMixin: object
    """
    __tablename__ = 'cagenix_role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description=None):
        """__init__ initializes a Role object given a name and description

        :param self: A Role Instance
        :type cls: class
        :param name: The name of the role being initialized
        :type name: string
        :param description: The description of the role being initialized
        :type description: string
        """
        self.name = name
        self.description = description

    def __repr__(self):
        """__repr__ specifies what a role looks like when viewed in the shell

        :param self: A Role Instance
        :type cls: class
        """
        return '<Role %r>' % self.name

    @classmethod
    def by_id(cls, role_id):
        """by_id returns a Role object given a role_id

        :param cls: The calling class
        :type cls: class
        :param role_id: The id of the role being searched for
        :type role_id: int
        """
        return db.session.query(Role).filter(Role.id == role_id).first()

    @classmethod
    def by_name(cls, role_name):
        """by_name returns a Role object given a role_name

        :param cls: The calling class
        :type cls: class
        :param role_name: The name of the role being searched for
        :type role_name: string
        """
        return db.session.query(Role).filter(Role.name == role_name).first()

    #  Query wrapper for UserCreate/EditForms
    @classmethod
    def get_roles(cls):
        """get_roles returns a list of Role objects

        This is primarily used by the WTForms to display the QueryMultipleSelect

        :param cls: The calling class
        :type cls: class
        """
        return db.session.query(Role)


class User(db.Model, UserMixin):
    """The User model defines the authentication users used by Flask-Security

    This Role class defines the model attributes, a classmethod to make finding
    the users easier. It also contains several fields unexposed by the UI. Those
    fields are used to track user logins and access IPs.

    :param db.Model: The SQLAlchemy base database model
    :type db.Model: object
    :param UserMixin: The UserMixin base provided by Flask-Security
    :type UserMixin: object
    """
    __tablename__ = 'cagenix_user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    activation_code = db.Column(db.String(255))
    address_one = db.Column(db.String(255))
    address_two = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip_code = db.Column(db.String(10))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    primary_color = db.Column(db.String(255))
    secondary_color = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    activated = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer())
    practice_id = db.Column(db.Integer, db.ForeignKey('cagenix_practice.id'), nullable=True)

    roles = db.relationship('Role', secondary=roles_users,
        backref=db.backref('cagenix_user', lazy='dynamic'))

    patients = db.relationship('Patient', backref='dentist', lazy='dynamic')

    #def __init__(self, username=None, password=None):
        #"""__init__ initializes a User object given a some info

        #:param self: A User Instance
        #:type cls: class
        #:param username: The username of the User being initialized
        #:type username: string
        #:param password: The password of the User being initialized
        #:type password: string
        #"""
        #self.username = username
        #self.password = password

    def __repr__(self):
        """__repr__ specifies what a role looks like when viewed in the shell

        :param self: A Role Instance
        :type cls: class
        """
        return '<User %r %r (%r)>' % (self.first_name, self.last_name, self.roles)

    @classmethod
    def by_id(cls, user_id):
        """by_id returns a User object given a user_id

        :param cls: The calling class
        :type cls: class
        :param user_id: The id of the user being searched for
        :type user_id: int
        """
        return db.session.query(User).filter(User.id == user_id).first()

    @classmethod
    def by_phone(cls, phone):
        """by_phone returns a User object given a phone number

        :param cls: The calling class
        :type cls: class
        :param phone: The phone number of the user being searched for
        :type phone: string
        """
        return db.session.query(User).filter(User.phone == phone).first()

    @classmethod
    def by_username(cls, username):
        """by_username returns a User object given a username

        :param cls: The calling class
        :type cls: class
        :param username: The username of the user being searched for
        :type username: string
        """
        return db.session.query(User).filter(User.username == username).first()

    @classmethod
    def by_email(cls, email):
        """by_email returns a User object given an email address.

        :param cls: The calling class
        :type cls: class
        :param email: The email of the user being searched for
        :type email: string
        """
        return db.session.query(User).filter(User.email == email).first()

    def map_data(self, data):
        ''' map_data takes a dict as an argument. It then iterates
        over each key field in the fields list, if a key is
        in the supplied dict, it will then update the attribute of
        this object to reflect the value of that key in the dict.

        The User implementation of map_data skips password to avoid plaintext
        compromises and security issues.
        '''

        fields = [
            'first_name', 'last_name', 'address_one', 'address_two', 'city',
            'state', 'zip_code', 'email', 'primary_color', 'secondary_color',
            'practice',
        ]

        for field in fields:
            if field in data:
                setattr(self, field, data[field])

    def gen_secret(self):
        ''' gen_secret creates a secret for the user.
        '''

        self.secret = hashlib.sha256(os.urandom(256) + datetime.datetime.utcnow().isoformat()).hexdigest()[:32]
