from user import User
from functools import wraps

def has_permission(required_permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, User):
                raise ValueError("First argument must be a User object")

            if user.has_permission(required_permission):
                return func(user, *args, **kwargs)
            else:
                print(f"🚫 Access Denied: User '{user.username}' does not have '{required_permission}' permission.")
                return None  

        return wrapper
    return decorator
