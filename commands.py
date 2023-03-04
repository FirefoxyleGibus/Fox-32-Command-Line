from component import *

def DIRCommand(curDir, *params):
    """Shows the content of a directory"""
    curDir.GetDirContent()
    print()
    return curDir

def AddDIR(curDir, params):
    """Adds a directory to the current directory"""
    print(f"Adding folder \"{params[1]}\" to \"{curDir.GetFuturePath()}\"\n")
    curDir.AddDir(params[1])
    return curDir

def RemoveDIR(curDir, params):
    """Removes a directory to the current directory"""
    print(f"Removing folder \"{params[1]}\" from \"{curDir.GetFuturePath()}\"\n")
    curDir.RemoveDir(params[1])
    return curDir

def ChangeCurDIR(curDir, params):
    """Changes the current directory"""
    print(f"Changing current directory to \"{curDir.content[params[1]].GetFuturePath()}\"\n")
    return curDir.content[params[1]]

def Help(curDir, params):
    """Shows all commands and describes them"""
    print("Showing help :")
    for i in commands.keys():
        print(f"{i:<10} : {commands[i].__doc__}")
    print()
    return curDir

commands = {"DIR":DIRCommand,
            "MKDIR":AddDIR,
            "MD":AddDIR,
            "RMVDIR":RemoveDIR,
            "RD":RemoveDIR,
            "CHDIR":ChangeCurDIR,
            "CD":ChangeCurDIR,
            "HELP":Help}