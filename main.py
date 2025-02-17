from Models.User import user

intro_text = """ 

Hello welcome to PyNano, a simple command-based text-editor. Please Login or Register to continue.
You can use the following commands:
Login 'USER'
Register
Exit

"""

def main():
    print(intro_text)
    current_user = None

    while True:
        command = input("Enter command: ").strip().lower()
        
        if command.startswith("login"):
            username = command.split(" ")[1]
            password = input("Enter password: ")
            current_user = user.User(username, "", password, "")  
            if current_user.login(username, password):
                print(f"Welcome back, {username}!")
                print(current_user)
            else:
                print("Invalid username or password.")
        
        elif command == "register":
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            new_user = user.User(username, email, password, "guest")
            new_user.register(username, email, password)
            print(f"User {username} registered successfully. Your role is 'guest'. This is the default role, set by the admin.")
        
        elif command == "exit":
            print("Exiting PyNano. Goodbye!")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

