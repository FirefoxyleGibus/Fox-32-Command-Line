from commands.exception import InvalidParameterException
from commands.command import *

class MakeDirectory(Command):
    def __init__(self, illegalName):
        super().__init__(['mkdir', 'md'])
        self.illegalNames = illegalName.copy()

    def run(self, curDir, params):
        if params[0] == "/?":
            return curDir, self.fullHelp()
        folders = " ".join(params).replace("/", "\\")
        if (self.IsNameValid(curDir, folders)):
            vitDir = curDir
            for folder in folders.split("\\"):
                vitDir.AddDir(folder)
                vitDir = vitDir.content[folder]
            return curDir, f"Adding folder \"{folders}\" to \"{curDir.GetFuturePath()}\"\n"
        else:
            return curDir, f"Folder \"{folders}\" cannot be created\n"
    
    def IsNameValid(self, curDir, name):
        return not (name in curDir or name in self.illegalNames)
    
    def help(self) -> str:
        return 'Creates a directory to the current directory'
    
    def fullHelp(self) -> str:
        return """Creates a directory to the current directory

MKDIR {path}
MD {path}

Example:
    MKDIR test - Will create a directory "test" in the current directory
    MKDIR AAA\\BBB - Will create the directory AAA with a directory BBB inside
"""
    
_md = MakeDirectory([])