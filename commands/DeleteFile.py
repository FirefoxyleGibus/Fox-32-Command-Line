from commands.exception import *
from commands.command import *

class DeleteFile(Command):
    def __init__(self):
        super().__init__(['del'])

    def run(self, curDir : Directory, params):
        if len(params) < 1:
            raise MissingParameterException("Missing parameter, see 'ADD /?' for usage.")
        if not params[0] in curDir.content.keys():
            raise InvalidParameterException(f"Cannot delete {params[0]}, file is missing.")
        del curDir.content[params[0]]
        return curDir, f"Deleting \"{params[0]}\" from \"{curDir.GetFuturePath()}\"\n"
    
    def help(self) -> str:
        return 'Delete a file from the current directory'
    
    def fullHelp(self) -> str:
        return """Delete a file from the current directory

DEL [filename]

Example:
    DEL test.txt - Delete test.txt from the current directory
"""

_del = DeleteFile()