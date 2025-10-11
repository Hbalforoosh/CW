
from abc import ABC, abstractmethod
import hashlib
from requerments import validate


class Person(ABC):
    def __init__(self, username, password):
        validate.validator_username(username)
        validate.validator_password(password)
        self._username = username
        self._password_hash = self._hash_password(password)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self._password_hash == self._hash_password(password)

    def change_password(self, old_pass, new_pass):
        if not self.check_password(old_pass):
            raise ValueError("Password incorrect")
        validate.validator_password(new_pass)
        self._password_hash = self._hash_password(new_pass)
        print("Change Password is successfully")

    @abstractmethod
    def dashboard(self):
        pass
