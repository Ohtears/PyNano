from Commands.base import BaseCommand
import os

BLUE = '\033[94m'  # Bright blue
WHITE = '\033[97m' # Bright white
RESET = '\033[0m'  # Reset color

class CDCommand(BaseCommand):
    def execute(self, session, *args):
        if not args:
            print('Please provide a directory to change to. "Usage: cd <directory>"')
        else:
            print("Changing to directory: ", args[0])
            # cd logic here

class LSCommand(BaseCommand):
    def execute(self, session, *args):
        print('These files exist in this directory')
        for item in sorted(os.listdir()):
            if os.path.isdir(item):
                print(f"{BLUE}{item}{RESET}")
            else:
                print(f"{WHITE}{item}{RESET}")

class PWDCommand(BaseCommand):
    def execute(self, session, *args):
        print('Current directory is:', os.getcwd())
        
class CreateCommand(BaseCommand):
    def execute(self, session, *args):
        if not args:
            print('Please provide a file to create. "Usage: create <filename>"')
        else:
            print(f'Creating file: {args[0]}')
            # Create logic here

class DelCommand(BaseCommand):
    def execute(self, session, *args):
        if not args:
            print('Please provide a file to delete. "Usage: del <filename>"')
        else:
            print(f'Deleting file: {args[0]}')
            # Delete logic here


