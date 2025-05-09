from Commands.base import BaseCommand
from Models.User.user_permissions import has_permission
from Interface.editor import Editor

class NanoCommand(BaseCommand):
    
    @has_permission('write')
    def execute(self, session, *args):
        if not args:
            print('Please provide a file to edit. Usage: nano <filename>')
        else:
            print(f'Opening file: {args[0]} in PyNano')
            editor = Editor(session)
            try:
                editor.open_file(args[0])
            except ValueError:
                print('Unsupported File Type')
                print('Try Again!')
                