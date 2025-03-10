from Interface.session_manager import SessionManager
from Core.registry import CommandRegistry
from Commands.dir_commands import CDCommand, LSCommand, PWDCommand, CreateCommand, DelCommand
from Commands.nano_command import NanoCommand

def main():

    CommandRegistry.register("cd", CDCommand())
    CommandRegistry.register("ls", LSCommand())
    CommandRegistry.register("nano", NanoCommand())
    CommandRegistry.register("pwd", PWDCommand())
    CommandRegistry.register("create", CreateCommand())
    CommandRegistry.register("del", DelCommand())

    session = SessionManager()
    session.run()
    


if __name__ == "__main__":
    main()

