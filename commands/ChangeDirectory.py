from commands.exception import *
from commands.command import Command

class ChangeDirectory(Command):
    def __init__(self):
        super().__init__(['chdir','cd'])

    def run(self, curDir, params):
        if len(params) < 0:
            raise MissingParameterException("Missing parameter, see 'CHDIR /?' for usage")

        toNavigateTo = curDir.ResolvePath(' '.join(params).replace('/', '\\'))
        if toNavigateTo == None:
            raise InvalidParameterException(f"Directory not found in \"{curDir.GetFuturePath()}\"\n")
        return toNavigateTo, f"Changing current directory to \"{toNavigateTo.GetFuturePath()}\"\n"
    
    def help(self) -> str:
        return 'Move to another directory from the current directory'
    
    def fullHelp(self) -> str:
        return """Move to another directory from the current directory

CHDIR {path}
CD {path}

Example:
    CD test - Will move to the directory "test" in the current directory
    CD AAA\\BBB - Will move to the directory BBB in the directory AAA
"""

_cd = ChangeDirectory()