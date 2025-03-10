class BaseCommand():
    def execute(self, session, *args):
        raise NotImplementedError("Each command must implement an execute method")
    
    # def undo(self, session):
    #     pass To be Determined