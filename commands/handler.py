from commands import _commands
from component import Directory
from commands.exception import *

def RunCommand(name : str, curDir : Directory, params: list[str]) -> Directory:
    """ Run a specified command """
    name = name.upper()
    if IsCommandAvailable(name):
        try:
            # handle help flag
            if len(params) > 1 and params[1] == "/?":
                print(_commands[name].fullHelp())
                return curDir
            # run command
            newCurDir, response = _commands[name].run(curDir, params[1:])
            print(response)
            return newCurDir
        # err checking
        except InvalidParameterException as err:
            print(f"[ERROR] {err}")
        except MissingParameterException as err:
            print(f"[ERROR] {err}")
            
    return curDir

def AvailableCommands() -> list[str]:
    """ Returns the list of registered commands """
    return _commands.keys()

def IsCommandAvailable(name : str) -> bool:
    """ Returns true if the command is registered """
    return name in _commands.keys()