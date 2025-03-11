import json
import hashlib
from pathlib import Path

from Core.Errors.exceptions import *

class User():

    #Constructor

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password__ = password
        self.role = role.lower()
        self.permissions = self.DEFAULT_ROLES.get(self.role, set())

    #Class Variables

    DEFAULT_ROLES = {
        "root": {"read", "write", "delete", "manage_users"},
        "admin": {"read", "write", "delete"},
        "editor": {"read", "write"},
        "guest": {"read"},
    }

    #Class Methods

    @classmethod
    def load_users(cls):
        file_path = Path(__file__).parent / '../user.json'
        with file_path.open('r') as file:
            data = json.load(file)
            cls.users = data['users']
            cls.default_role = data.get('default_user', 'guest')

    @classmethod
    def save_users(cls):
        file_path = Path(__file__).parent / '../user.json'
        with file_path.open('w') as file:
            json.dump({"default_user": cls.default_role, "users": cls.users}, file, indent=4)

    @classmethod
    def update_default_role(cls, new_role):
        if new_role in cls.DEFAULT_ROLES:
            cls.default_role = new_role
            cls.save_users()
            print(f"Default role updated to {new_role}.")
        else:
            print(f"Role {new_role} does not exist.")


    #Methods

    def has_permission(self, action):
        return action in self.permissions

    def register(self, username, email, password):
        if not any(user['username'] == username for user in self.users):
            new_user = {
                "username": username,
                "email": email,
                "password": hashlib.sha256(password.encode()).hexdigest(),
                "role": self.default_role
            }
            self.users.append(new_user)
            self.save_users()
            return
        raise UserAlreadyExistsError

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user['username'] == username:
                if user['password'] == hashed_password or password == user['password']:
                    self.__init__(user['username'], user['email'], user['password'], user['role'])
                    return 
                raise IncorrectPasswordError
        raise UserNotFoundError

    def reset_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user['username'] == self.username:
                user['password'] = hashed_password
                self.save_users()
                return


    #Magic Methods

    def __str__(self):
        return f"User({self.username}, role={self.role})"

    #Getters and Setters

    def get_all_users(self) -> list:
        return self.users

User.load_users()