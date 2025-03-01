__all__ = ["UserAlreadyExistsError", "UserNotFoundError", "IncorrectPasswordError"]

class UserError(Exception):
    pass

class UserNotFoundError(UserError):
    pass
class IncorrectPasswordError(UserError):
    pass
class UserAlreadyExistsError(UserError):
    pass