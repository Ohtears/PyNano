from Models.User.user import User
from functools import wraps

def has_permission(required_permission):
    def decorator(func):
        @wraps(func)
        def wrapper(self, session, *args, **kwargs):
            user = session.current_user
            if not user:
                print("⚠️ No user logged in.")
                return

            if not hasattr(user, "has_permission"):
                raise ValueError("Session's current_user must implement `has_permission`")

            if user.has_permission(required_permission):
                return func(self, session, *args, **kwargs)
            else:
                print(f"🚫 Access Denied: User '{user.username}' does not have '{required_permission}' permission.")
        return wrapper
    return decorator
