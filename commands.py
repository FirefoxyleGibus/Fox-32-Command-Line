from component import *

def IsPathValid(curDir, path):
    vitDir = curDir
    try:
        for folder in path.split("\\"):
            vitDir = vitDir.content[folder]
        return True
    except KeyError:
        return False

# TODO : Clean the code with class

def DIRCommand(curDir, *params):
    """Shows the content of a directory"""
    curDir.GetDirContent()
    print()
    return curDir

def AddDIR(curDir, params):
    """Adds a directory to the current directory"""
    folders = " ".join(params[1:]).replace("/", "\\")
    vitDir = curDir
    for folder in folders.split("\\"):
        vitDir.AddDir(folder)
        vitDir = vitDir.content[folder]
    print(f"Adding folder \"{folders}\" to \"{curDir.GetFuturePath()}\"\n")
    return curDir

def RemoveDIR(curDir, params):
    """Removes a directory to the current directory"""
    folderName = " ".join(params[1:])
    if (IsPathValid(curDir, folderName)):
        print(f"Removing folder \"{folderName}\" from \"{curDir.GetFuturePath()}\"\n")
        curDir.RemoveDir(folderName)
    else:
        print(f"Folder \"{folderName}\" doesn't exist !\n")
    return curDir

def ChangeCurDIR(curDir, params):
    """Changes the current directory"""
    path = " ".join(params[1:]).replace("/", "\\")
    if (IsPathValid(curDir, path)):
        newDir = curDir
        for folder in path.split("\\"):
            newDir = newDir.content[folder]
        print(f"Changing current directory to \"{newDir.GetFuturePath()}\"\n")
        return newDir
    else:
        print(f"Requested directory doesn't exist !\n")
        return curDir
        

def AddFile(curDir, params):
    """Add a file to the current directory"""
    fileName = " ".join(params[1:])
    print(f"Adding file \"{fileName}\" to \"{curDir.GetFuturePath()}\"\n")
    match (fileName.split(".")[1].upper()):
        case "TXT":
            TextFile("", fileName, "").PutFileOnDir(curDir)
        case _:
            File("", fileName, "").PutFileOnDir(curDir)
    return curDir

def DeleteFile(curDir, params):
    """Delete the file from the current directory"""
    print(f"Deleting \"{params[1]}\" from \"{curDir.GetFuturePath()}\"\n")
    del curDir.content[params[1]]
    return curDir

def TypeFile(curDir, params):
    """Types the content of a file in the shell"""
    fileName = " ".join(params[1:])
    curDir.content[fileName].TypeContent()
    print()
    return curDir

def RunFile(curDir, params):
    """Executes the file"""
    fileName = " ".join(params[1:])
    curDir.content[fileName].ExecuteFunction()
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
            "RUN":RunFile,
            "HELP":Help}

programs = {}