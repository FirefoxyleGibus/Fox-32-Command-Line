"""

Commands module

Loads every commands found in this directory into `_commands`

Usage: 
* Import the handler
    from commands.handler import *
* You have now access to these functions:
    RunCommand(name: str, params : list[str])
    AvailableCommandNames() -> list[str]
    IsCommandAvailable(name : str) -> bool

"""

# Contains all loaded/registered commands
_commands = {}

def _load():
    """ 
        Do not class or import 
        Load the content of this dir and import them
    """
    import os, importlib
    commands_path = f"{os.curdir}/commands"
    for file in os.listdir(commands_path):
        file_abs = os.path.abspath(commands_path + "/" + file)
        if os.path.isfile(file_abs) and file != "__init__.py":
            p, m = file.rsplit('.', 1)
            print(f"[DEBUG] Loading : {p}")
            mod = importlib.import_module(f"commands.{p}")

# load
_load()