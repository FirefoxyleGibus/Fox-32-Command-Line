from commands.exception import InvalidParameterException
from commands.command import *
from commands import _commands

class HelpClass(Command):
    def __init__(self):
        super().__init__(['help'])

    def run(self, curDir, params):
        if len(params) > 0:
            if params[0] == "/?":
                return curDir, self.fullHelp()
        output = "Showing help ! Use /? after a command to get more info."
        maxComLen = 0
        for com in _commands.keys():
            maxComLen = max(len(com), maxComLen)
        for com in _commands.keys():
            output += f"{com:<{maxComLen}} : {_commands[com].help()}\n"
        return curDir, output
    
    def IsNameValid(self, curDir, name):
        return not (name in curDir or name in self.illegalNames)
    
    def help(self) -> str:
        return 'Shows this help text'
    
    def fullHelp(self) -> str:
        return """Shows help about all commands

Use the /? argument on any command to get more information
"""
    
_help = HelpClass()