from component import *
from commands import *

DiskA = Disk("A:","Main","0001-0F2C")
curpath = DiskA
prompt = "> "

while(1):
    A = input(prompt)
    instr = A.split(" ")
    
    if (instr[0].upper() in commands.keys()):
        curpath = commands[instr[0].upper()](curpath, instr)
    elif (instr[0].upper() == "EXIT"):
        break