from commands.exception import *
from commands.command import Command

class ChangeDirectory(Command):
    def __init__(self):
        super().__init__(['cd'])

    def run(self, curDir, params):
        if len(params) < 0:
            raise MissingParameterException("Missing parameter, see 'MKDIR /?' for usage")

        toNavigateTo = curDir.ResolvePath(' '.join(params).replace('/', '\\'))
        if toNavigateTo == None:
            raise InvalidParameterException(f"Directory not found in \"{curDir.GetFuturePath()}\"\n")
        return toNavigateTo, f"Moved to {toNavigateTo.GetFuturePath()}"
    
    def help(self) -> str:
        return 'Move to another directory from the current directory'
    
    def fullHelp(self) -> str:
        return """Move to another directory from the current directory

CD {path}

Example:
    CD test - Will move to the directory "test" in the current directory
    CD AAA\\BBB - Will move to the directory BBB in the directory AAA
"""

_cd = ChangeDirectory()