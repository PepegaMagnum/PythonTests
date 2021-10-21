import hashlib
import hmac


class Utility:

    @staticmethod
    def generate_hash(url, key_encoded):
        msg = "<url>"+url+"</url>"
        secret_key_spec = hmac.new(key_encoded.encode(), msg.encode(), hashlib.sha256).hexdigest()
        return secret_key_spec
