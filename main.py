from component import Disk,Directory,File,TextFile, ProgramFile
from commands import *
from datetime import datetime

DiskA = Disk("A:","Main","FF45-01a4", datetime(day=4, month=3, year=2023, hour=21, minute=38))
DiskA.AddDir("PROGRAMS", datetime(day=4, month=3, year=2023, hour=21, minute=38))
DiskA.AddDir("USERS", datetime(day=5, month=3, year=2023, hour=9, minute=49))
TextFile("","LOG.TXT","""04/03/2023 : Added LOG file !
05/03/2023 : Added ADD and DEL
05/03/2023 : Added Programs
06/03/2023 : Optimizing the shell""", 0, datetime(day=4, month=3, year=2023, hour=21, minute=38)).PutFileOnDir(DiskA.content["PROGRAMS"])
ProgramFile("", "TEST.CLEXE", lambda *params : print("Test function !"), 10).PutFileOnDir(DiskA.content["PROGRAMS"])
curpath = DiskA
prompt = "%P > "

def GeneratePrompt(content):
    out = ""
    pourcent = False
    for letter in content.lower():
        if (pourcent):
            if (letter == 'p'):
                out += curpath.GetFuturePath()
            elif (letter == '%'):
                out += '%'
            pourcent = False
        else:
            if (letter != '%'):
                out += letter
            else:
                pourcent = True
    return out

print("Welcome to Fox-32 Command Line (Fox-32 CL) !\nPress HELP to get help !")

while(1):
    A = input(GeneratePrompt(prompt))
    instr = A.split(" ")
    
    files = [i.name for i in curpath]
    
    
    if IsCommandAvailable(instr[0].upper()):
        curpath = RunCommand(instr[0], curpath, instr)
    elif instr[0].upper() == 'HELP':
        print(AvailableCommands())
    # elif (instr[0].upper() in programs.keys()):
    #     pass
    elif (instr[0] in files):
        if (type(curpath.content[instr[0]]) == ProgramFile):
            curpath.content[instr[0]].ExecuteFunction()
        else:
            print(f"\"{instr[0].upper()}\" is not a valid command/program !\n")
    elif (instr[0].upper() == "EXIT"):
        break
    else:
        print(f"\"{instr[0].upper()}\" is not a valid command/program !\n")
