from Models.User import user
from Interface.SessionManager import SessionManager

def main():

    session = SessionManager()
    session.run()
    
if __name__ == "__main__":
    main()

