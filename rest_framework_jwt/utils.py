import jwt
import datetime

from .settings import api_settings


def jwt_payload_handler(user):
    return {
        'user_id': user.id,
        'email': user.email,
        'username': user.username,
        'exp': datetime.datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }


def jwt_encode_handler(payload):
    return jwt.encode(
        payload,
        api_settings.JWT_SECRET_KEY,
        api_settings.JWT_ALGORITHM
    )


def jwt_decode_handler(token):
    return jwt.decode(
        token,
        api_settings.JWT_SECRET_KEY,
        api_settings.JWT_VERIFY,
        api_settings.JWT_VERIFY_EXPIRATION,
        api_settings.JWT_LEEWAY
    )