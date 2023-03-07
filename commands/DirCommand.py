from commands.exception import InvalidParameterException
from commands.command import *

class DirCommand(Command):
    def __init__(self):
        super().__init__(['dir'])

    def run(self, curDir : Directory, params):
        toList = curDir
        if len(params) > 0:
            toList = curDir.ResolvePath(params[0])
        if toList == None:
            raise InvalidParameterException(f"Folder {params[0]} doesn't exist")
        return curDir, toList.GetDirContent()
    
    def help(self) -> str:
        return 'Displays a list of files and subdirectories in a directory.'
    
    def fullHelp(self) -> str:
        return """Displays a list of files and subdirectories in a directory.

DIR [path]

Example:
    DIR - Displays a list of files and subdirectories of the current directory
    DIR AAA - Displays a list of files and subdirectories in the directory AAA
"""
    
    def __str__(self):
        return super().__str__() + " [path]: List content of current dir\n" + "- [path] (optionnal) path to the directory to list"

_dir = DirCommand()