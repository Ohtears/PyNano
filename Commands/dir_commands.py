from Commands.base import BaseCommand
from Models.User.user_permissions import has_permission

from pathlib import Path


BLUE = '\033[94m'  # Bright blue
WHITE = '\033[97m' # Bright white
RESET = '\033[0m'  # Reset color

class CDCommand(BaseCommand):
    def execute(self, session, *args):
        if not args:
            print('Please provide a directory to change to. "Usage: cd <directory>"')
            return 
        
        else:
            target_path = Path(session.current_dir) / args[0]
            if target_path.is_dir():
                session.current_dir = str(target_path.resolve())
                print(f"Moved to {session.current_dir}")
            else:
                print("Directory does not exist.")
    
class LSCommand(BaseCommand):
    def execute(self, session, *args):
        print("These files exist in this directory:")
        items = sorted(Path(session.current_dir).iterdir())
        for item in items:
            if item.is_dir():
                print(f"{BLUE}{item.name}{RESET}")
            else:
                print(f"{WHITE}{item.name}{RESET}")

class PWDCommand(BaseCommand):
    def execute(self, session, *args):
        print('Current directory is:', session.current_dir)
        
class CreateCommand(BaseCommand):
    @has_permission('write')
    def execute(self, session, *args):
        if not args:
            print('Please provide a file to create. "Usage: create <filename>"')
            return
        else:
            print(f'Creating file: {args[0]}')
            target_path = Path(session.current_dir) / args[0]
            try:
                target_path.touch()
                print('File created.')
            except FileExistsError:
                print('File already exists.')

class DelCommand(BaseCommand):
    @has_permission('delete')
    def execute(self, session, *args):
        if not args:
            print('Please provide a file to delete. "Usage: del <filename>"')
            return
        else:
            print(f'Deleting file: {args[0]}')
            target_path = Path(session.current_dir) / args[0]

            try:
                target_path.unlink()
                print(f"File deleted: {target_path.name}")
            except FileNotFoundError:
                print("File does not exist.")
            except IsADirectoryError:
                print("Cannot delete a directory.")


