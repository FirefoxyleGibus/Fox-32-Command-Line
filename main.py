from component import Disk,Directory,File,TextFile
from commands import commands
from datetime import datetime

DiskA = Disk("A:","Main","FF45-01a4", datetime(day=4, month=3, year=2023, hour=21, minute=38))
DiskA.AddDir("PROGRAMS", datetime(day=4, month=3, year=2023, hour=21, minute=38))
DiskA.AddDir("USERS", datetime(day=5, month=3, year=2023, hour=9, minute=49))
TextFile("","LOG.TXT","""04/03/2023 : Added LOG file !
05/03/2023 : Added ADD and DEL""", 0, datetime(day=5, month=3, year=2023, hour=10, minute=23)).PutFileOnDir(DiskA.content["PROGRAMS"])
curpath = DiskA
prompt = "> "

print("Welcome to Fox-32 Command Line (Fox-32 CL) !\nPress HELP to get help !")

while(1):
    A = input(prompt)
    instr = A.split(" ")
    
    if (instr[0].upper() in commands.keys()):
        curpath = commands[instr[0].upper()](curpath, instr)
    elif (instr[0].upper() == "EXIT"):
        break