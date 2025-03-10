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


