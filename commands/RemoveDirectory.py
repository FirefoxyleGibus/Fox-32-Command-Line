from commands.exception import *
from commands.command import Command

class RemoveDirectory(Command):
    def __init__(self):
        super().__init__(['rmvdir', 'rd'])

    def run(self, curDir, params):
        if len(params) < 1:
            raise MissingParameterException("Missing parameter, see 'RMVDIR /?' for usage")

        path = ' '.join(params).replace('/', '\\')
        toRemove = curDir.ResolvePath(path)
        if toRemove == None:
            raise InvalidParameterException(f"Cannot remove non-existing folder \"{path}\" from \"{curDir.GetFuturePath()}\"\n")
        
        folderName = toRemove.name
        curDir.RemoveDir(folderName)
        return curDir, f"Removed folder \"{folderName}\" from \"{curDir.GetFuturePath()}\" \n"
    
    def help(self) -> str:
        return 'Remove a directory from the current directory'
    
    def fullHelp(self) -> str:
        return """Remove a directory from the current directory

RMVDIR {path}
RD {path}

Example:
    RMVDIR test - Will delete a directory "test" in the current directory
    RMVDIR AAA\\BBB - Will delete the directory BBB in the directory AAA
"""

_rd = RemoveDirectory()