from commands.exception import MissingParameterException
from commands.command import *

class TypeFile(Command):
    def __init__(self):
        super().__init__(['type'])

    def run(self, curDir : Directory, params):
        if len(params) < 1:
            raise MissingParameterException("Missing parameter, see 'TYPE /?' for usage.")
        fileName = " ".join(params)
        return curDir, curDir.content[fileName].TypeContent()
    
    def help(self) -> str:
        return 'Types the content of a file in the shell'
    
    def fullHelp(self) -> str:
        return """Types the content of a file in the shell

TYPE {filename}

Example:
    Type test.txt - Print the content of test.txt in the shell
"""
    
_type = TypeFile()