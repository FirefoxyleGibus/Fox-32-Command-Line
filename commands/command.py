from component import Directory
from commands.exception import InvalidParameterException
from commands import _commands

""" Base command class """
class Command:
    def __init__(self, alias: list[str]):
        self.aliases = alias.copy()
        for a in self.aliases:
            a = a.upper()
            if a in _commands.keys():
                print(f"[ERROR] Alias '{a}' already defined for {_commands[a].__class__.__name__}")
                continue
            _commands[a] = self

    def run(self, curDir: Directory, params: list[str]) -> tuple[Directory, str]:
        """ Run the command using params
        Params:
            curDir (Directory) : Current directory where we are
            params (list[str]) : list of params of the command line
        Returns:
            tuple[Directory, str] which correspond to (new Current Directory, Command log)
        """
        return curDir, 'Nothing was done'

    def __repr__(self):
        return f'[Command {", ".join(self.aliases)}]'

    def __str__(self):
        return f'Usage for {self.aliases[0]}'