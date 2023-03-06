from component import Directory
from commands.exception import InvalidParameterException
from commands import _commands

class Command:
    def __init__(self, alias: list[str]):
        self.aliases = alias.copy()
        for a in self.aliases:
            _commands[a.upper()] = self

    def run(self, curDir: Directory, params: list[str]) -> tuple[Directory, str]:
        return curDir, 'Nothing was done'

    def __repr__(self):
        return f'[Command {", ".join(self.aliases)}]'

    def __str__(self):
        return f'Usage {self.name}'