from Commands.base import BaseCommand

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

class PWDCommand(BaseCommand):
    def execute(self, session, *args):
        print('Current directory is: ')
        # PWD LOGIC here

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


