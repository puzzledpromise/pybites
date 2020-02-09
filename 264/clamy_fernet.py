import os
import base64
from cryptography.fernet import Fernet  # type: ignore
from cryptography.hazmat.backends import default_backend  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
from os import urandom
from typing import ByteString, Tuple, Optional


class ClamyFernet:
    """Fernet implementation by clamytoe

    Takes a bytestring as a password and derives a Fernet
    key from it. If a key is provided, that key will be used.

    :param password: ByteString of the password to use
    :param key: ByteString of the key to use, else defaults to None

    Other class variables that you should implement that are hard set:

    salt, algorithm, length, iterations, backend, and generate a base64
    urlsafe_b64encoded key using self.clf().
    """

    def __init__(self, password=b"pybites", key=None):
        self.password = password
        self.salt = os.urandom(16)
        self.algorithm = hashes.SHA256()
        self.length = 32
        self.iterations = 100000 
        self.backend = default_backend()
        if key is not None:
            self.key = key
        else:
            self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        


    @property
    def kdf(self):
        """Derives the key from the password

        Uses PBKDF2HMAC to generate a secure key. This is where you will
        use the salt, algorithm, length, iterations, and backend variables.
        """
        return PBKDF2HMAC(
                algorithm=self.algorithm,
                length=self.length,
                salt=self.salt,
                iterations=self.iterations,
                backend=self.backend
        )


    @property
    def clf(self):
        """Generates a Fernet object

        Key that is derived from cryptogrophy's fermet.
        """
        return Fernet(self.key)

    def encrypt(self, message: str) -> ByteString:
        """Encrypts the message passed to it"""
        return Fernet(self.key).encrypt(message.encode("utf-8"))

    def decrypt(self, token: ByteString) -> str:
        """Decrypts the encrypted message passed to it"""
        return self.clf.decrypt(token).decode("utf-8")

if __name__ == "__main__":
    key=b"rvxePMSDUcZFowEaNxnFb8Pifn1KmhkF70Mz1ZQe2Bw="
    clm = ClamyFernet(key=key)
    enc = clm.encrypt(b"Hello world")
    print(clm.decrypt(enc))
