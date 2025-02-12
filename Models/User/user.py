class User():

    users = ["root", "admin", "editor", "guest"]

    default_role = "guest"

    DEFAULT_ROLES = {
        "root": {"read", "write", "delete", "manage_users"},
        "admin": {"read", "write", "delete"},
        "editor": {"read", "write"},
        "guest": {"read"},
    }

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password__ = password
        self.role = role.lower()
        self.permissions = self.DEFAULT_ROLES.get(self.role, set())

    @classmethod
    def update_default_role(cls, new_role):
        cls.default_role = new_role

    def has_permission(self, action):
        return action in self.permissions

    def login(self, username, password):
        pass

    def register(self, username, email, password):
        pass

    def __str__(self):
        return f"User({self.username}, role={self.role})"

    def get_all_users(self) -> list:
        return self.users


    
