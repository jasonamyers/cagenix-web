import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['jason@jasonamyers.com'])
SECRET_KEY = 'SessionKey'

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'CSRFKey'

API_KEY = ''
API_SECRET =i ''

PASSPHRASE = 'Sc0z8Lq2O0b76jOR_X>PTLhK'

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'postmaster@app20961882.mailgun.org'
MAIL_PASSWORD = '6myh48wc-mp2'
MAIL_DEFAULT_SENDER = 'postmaster@app20961882.mailgun.org'

SECURITY_EMAIL_SENDER = 'postmaster@app20961882.mailgun.org'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'wRfoeFqqD7ULQcU6ixdX'
SECURITY_UNAUTHORIZED_VIEW = None
SECURITY_CONFIRMABLE = False
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CONFIRM_SALT = '7wF7mKhtQMNCBQydMrgY'
SECURITY_REMEMBER_SALT = 'XYaEAPkYBs7tKF9LfqPH'
SENTRY_DSN = ''

AWS_LOCATION = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_DIRECTORY = ''
