from Commands.base import BaseCommand
from Models.User.user import User
from Models.User.user_permissions import has_permission

class NanoCommand(BaseCommand):
    
    @has_permission('write')
    def execute(self, session, *args):
        if not args:
            print('Please provide a file to edit. Usage: nano <filename>')
        else:
            print(f'Opening file: {args[0]} in PyNano')
  