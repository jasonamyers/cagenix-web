import base64
import hashlib
import hmac

from passlib.hash import pbkdf2_sha512


def encrypt_password(password):
    from config import SECURITY_PASSWORD_SALT
    h = hmac.new(SECURITY_PASSWORD_SALT.encode('utf-8'), password.encode('utf-8'), hashlib.sha512)
    signed = base64.b64encode(h.digest()).decode('ascii')
    return pbkdf2_sha512.encrypt(signed)
