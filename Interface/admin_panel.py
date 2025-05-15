from Interface.session_manager import SessionManager
from Models.User.user_permissions import has_permission
from Models.User.user import User

class AdminPanel(SessionManager):
    def __init__(self, session: SessionManager):
        super().__init__()
        self.session = session
        self.current_user = session.current_user
        self.running = True

    @has_permission("manage_users")
    def run(self, session):
        print("\nWelcome to the Admin Panel.")
        print("Available commands: list_users | grant <username> <role> | revoke <username> | back")

        while self.running:
            command = input("admin>> ").strip().lower()
            parts = command.split()

            if not parts:
                continue
            cmd, *args = parts

            if cmd == "list_users":
                self.list_users()
            elif cmd == "grant" and len(args) == 2:
                self.grant_permission(args[0], args[1])
            elif cmd == "revoke" and len(args) == 1:
                self.revoke_permission(args[0])
            elif cmd == "back":
                self.running = False
            else:
                print("Unknown command.")

    def list_users(self):
        for user in self.current_user.get_all_users():
            print(f"{user['username']} ({user['role']}): {user.get('permissions', User.DEFAULT_ROLES.get(user['role'], []))}")

    def grant_permission(self, username, role):
        if role not in User.DEFAULT_ROLES:
            print(f"Invalid role '{role}'. Valid roles are: {', '.join(User.DEFAULT_ROLES.keys())}.")
            return

        for user in self.current_user.users:
            if user["username"] == username:
                user["role"] = role
                User.save_users()
                print(f"Assigned role '{role}' to {username}.")
                return
        print(f"User '{username}' not found.")

    def revoke_permission(self, username):
        for user in self.current_user.users:
            if user["username"] == username:
                user_role = user["role"]
                print(f"Revoked {user_role} from {username}. {username} is now a guest")
                user["role"] = "guest"
                User.save_users()
                return
        print(f"User '{username}' not found or has no permissions.")
