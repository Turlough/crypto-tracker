# authorization class to access portfolio API

import base64
import hashlib
import hmac
import time

from requests.auth import AuthBase


class Auth(AuthBase):

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):  # format call for Coinbase API
        timestamp = str(int(time.time()))
        message = timestamp + request.method + request.path_url + (request.body or '')
        secret = self.secret_key

        if not isinstance(message, bytes):
            message = message.encode()
        if not isinstance(secret, bytes):
            secret = secret.encode()

        signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
        request.headers.update({
            # to_native_string('CB-VERSION'): self.api_version,
            to_native_string('CB-ACCESS-KEY'): self.api_key,
            to_native_string('CB-ACCESS-SIGN'): signature,
            to_native_string('CB-ACCESS-TIMESTAMP'): timestamp,
        })
        return request


def to_native_string(string, encoding='ascii'):
    """Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise.
    """
    if isinstance(string, str):
        out = string

    return out
