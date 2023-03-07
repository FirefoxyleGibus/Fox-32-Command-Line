from commands.exception import *
from commands.command import *
from component import ProgramFile
from time import process_time

class RunFile(Command):
    def __init__(self):
        super().__init__(['run'])

    def run(self, curDir : Directory, params):
        if len(params) < 1:
            raise MissingParameterException("Missing parameter, see 'RUN /?' for usage.")
        fileName = " ".join(params)
        if not fileName in curDir.content.keys():
            raise InvalidParameterException(f"Cannot run {fileName}, file is missing")
        t0 = process_time()
        if isinstance(curDir.content[fileName], ProgramFile): 
            curDir.content[fileName].ExecuteFunction()
            print()
        timeDiff = process_time() - t0
        return curDir, f'Executed {fileName} in {timeDiff:.2f}s'
    
    def help(self) -> str:
        return 'Run a file in the current directory'
    
    def fullHelp(self) -> str:
        return """Run a file in the current directory

Run [filename] [args]

Example:
    Run test squaboubla - Run test in the current directory with the param 'squaboubla'
"""
    
_run = RunFile()