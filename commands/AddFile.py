from commands.exception import MissingParameterException
from commands.command import *

class AddFile(Command):
    def __init__(self):
        super().__init__(['add'])

    def run(self, curDir : Directory, params):
        if len(params) < 1:
            raise MissingParameterException("Missing parameter, see 'ADD /?' for usage.")
        fileName = " ".join(params)
        match (fileName.split(".")[1].upper()):
            case "TXT":
                TextFile("", fileName, "").PutFileOnDir(curDir)
            case _:
                File("", fileName, "").PutFileOnDir(curDir)
        return curDir, f"Adding file \"{fileName}\" to \"{curDir.GetFuturePath()}\"\n"
    
    def help(self) -> str:
        return 'Add a file to the current directory'
    
    def fullHelp(self) -> str:
        return """Add a file to the current directory

ADD [filename]

Example:
    ADD test.txt - Add test.txt to the current directory
"""

_add = AddFile()