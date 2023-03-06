"""

Commands module

Loads every commands found in this directory into `_commands`

Usage:
    RunCommand(name: str, params : list[str])
    AvailableCommandNames() -> list[str]
    IsCommandAvailable(name : str) -> bool

"""
from component import Directory
from commands.exception import InvalidParameterException

_commands = {}

def RunCommand(name : str, curPath : str, params: list[str]) -> Directory:
    name = name.upper()
    if IsCommandAvailable(name):
        try:
            newCurDir, response = _commands[name].run(curPath, params[1:])
            print(response)
            return newCurDir
        except InvalidParameterException as err:
            print(f"[ERROR] {err}")
    return curPath

def AvailableCommands() -> list[str]:
    return _commands.keys()

def IsCommandAvailable(name : str) -> bool:
    return name in _commands.keys()


def _load():
    import os, importlib
    commands_path = f"{os.curdir}/commands"
    for file in os.listdir(commands_path):
        file_abs = os.path.abspath(commands_path + "/" + file)
        if os.path.isfile(file_abs) and file != "__init__.py":
            p, m = file.rsplit('.', 1)
            print(f"[DEBUG] Loading : {p}")
            mod = importlib.import_module(f"commands.{p}")

_load()