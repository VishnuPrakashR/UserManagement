#  Copyright (c) 2023. This is the property of Vishnu Prakash
from passlib.context import CryptContext


class Password:
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )

    def encrypt(self, password):
        return self.pwd_context.encrypt(password)

    def verify(self, password, hashed):
        return self.pwd_context.verify(password, hashed)

