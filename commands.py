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

def AddFile(curDir, params):
    """Add a file to the current directory"""
    print(f"Adding file \"{params[1]}\" to \"{curDir.GetFuturePath()}\"\n")
    match (params[1].split(".")[1].upper()):
        case "TXT":
            TextFile("", params[1], "").PutFileOnDir(curDir)
        case _:
            File("", params[1], "").PutFileOnDir(curDir)
    return curDir

def DeleteFile(curDir, params):
    """Delete the file from the current directory"""
    print(f"Deleting \"{params[1]}\" from \"{curDir.GetFuturePath()}\"\n")
    del curDir.content[params[1]]
    return curDir

def TypeFile(curDir, params):
    """Types the content of a file in the shell"""
    curDir.content[params[1]].TypeContent()
    print()
    return curDir

def Help(curDir, params):
    """Shows all commands and describes them"""
    print("Showing help :")
    for i in commands.keys():
        print(f"{i:<10} : {commands[i].__doc__}")
    print(f'{"EXIT":<10} : Exits the shell\n')
    return curDir

commands = {"DIR":DIRCommand,
            "MKDIR":AddDIR,
            "MD":AddDIR,
            "RMVDIR":RemoveDIR,
            "RD":RemoveDIR,
            "CHDIR":ChangeCurDIR,
            "CD":ChangeCurDIR,
            "ADD":AddFile,
            "DEL":DeleteFile,
            "TYPE":TypeFile,
            "HELP":Help}