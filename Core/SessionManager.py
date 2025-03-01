from Models.User.user import User 
from Core.Errors.exceptions import *

class SessionManager:
    
    intro_text = """ 

    Hello welcome to PyNano, a simple command-based text-editor. Please Login or Register to continue.
    You can use the following commands:
    Login 'USER'
    Register
    Exit

    """
    #Constructor

    def __init__(self):
        self.current_user = None
        self.command = None

    @property
    def current_user(self) -> User:
        if self.current_user is None:
            raise ValueError('No user is logged in')
        return self.current_user

    #Methods

    def run(self):
        while True:
            if self.current_user is None:
                self.show_main_menu()
            else:
                self.show_dashboard()
    
    def show_main_menu(self):
        print(self.intro_text)
        command = input(">>").strip().lower()

        match command:
            case "login":
                self.login()
            case "register":
                self.register()
            case "exit":
                print("Exiting PyNano. Goodbye!")
            case _:
                print("Unknown command. Please try again.")

    def show_dashboard(self):
        pass

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
            print(current_user)
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