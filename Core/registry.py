class CommandRegistry:
    _commands = {}

    @classmethod
    def register(cls, name, command):
        cls._commands[name] = command

    @classmethod
    def get(cls, name):
        return cls._commands.get(name, None)
