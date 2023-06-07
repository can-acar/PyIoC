from model import Model


class SampleRequest(Model):
    test_key: str
    test_value: str
    _properties = {
        "username": {
            "type": str,
            "error": "Username must be a string"
        },
        "password": {
            "type": str,
            "error": "Password must be a string"
        },
        "email": {
            "type": str,
            "error": "Email must be a string"
        }
    }
