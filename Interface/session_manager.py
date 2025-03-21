from Models.User.user import User 
from Core.Errors.exceptions import *
from Core.registry import CommandRegistry

from pathlib import Path

class SessionManager:
    
    intro_text = """ 

Hello welcome to PyNano, a simple command-based text-editor. Please Login or Register to continue.
You can use the following commands:
login 'USER'
register
exit

    """

    dashboard_text = """

Welcome to PyNano, a simple command-based text-editor. You can use the following commands:
cd 'DIRECTORY'
pwd
ls 
create 'FILE'
nano 'FILE'
del 'FILE'
logout
change password
exit

    """

    #Constructor

    def __init__(self):
        self.current_user = None
        self.command = None
        self.current_dir = Path.cwd()
        
    #Methods

    def run(self):
        while True:
            if self.current_user is None:
                self.show_main_menu()
            else:
                self.show_dashboard()
    
    def show_main_menu(self):
        print(self.intro_text)
        self.command = input(">> ").strip().lower()

        if self.command.startswith('login'):
            self.login()
        elif self.command == 'register':
            self.register()
        elif self.command == 'exit':
            print("Exiting PyNano...")
            exit()
        else:
            print("Unknown command. Please try again.")

    def show_dashboard(self):
        self.command = input(">> ").strip()

        cmd = self.command.split(" ")[0].lower()
        args = self.command.split(" ")[1:]

        if cmd == 'logout':
            self.logout()
        elif cmd == 'change password' and args[0] == 'password':
            self.change_password()
        elif cmd == 'exit':
            print('Exiting PyNano...')
            exit() 
        
        else:
            command = CommandRegistry.get(cmd)
            if command:
                command.execute(self, *args)
            else:
                print("Unknown command. Please try again.")


    def register(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        new_user = User(username, email, password, "guest")
        try:
            new_user.register(username, email, password)
            print(f"User {username} registered successfully. Your role is 'guest'. This is the default role, set by the admin.")
        except UserAlreadyExistsError:
            print(f"User {username} already exists. Please try again.")
    
    def login(self):
        username = self.command.split(" ")[1]
        password = input("Enter password: ")
        current_user = User(username, "", password, "")  
        try:
            current_user.login(username, password)
            print(f"Welcome back, {username}!")
            print(self.dashboard_text)
            self.current_user = current_user
        except IncorrectPasswordError:
            print("Incorrect password. Please try again.")
        except UserNotFoundError:
            print(f"User {username} not found. Please try again.")
        
    def logout(self):
        self.current_user = None
        print("Logged out successfully.")

    def change_password(self):
        password = input("Enter new password: ")
        self.current_user.reset_password(password)