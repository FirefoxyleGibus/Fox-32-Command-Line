from datetime import datetime

class MainFileClass():
    """A simple file
    Can either be a file or a folder
    Only used as a parent class"""
    
    def __init__(self, p, n, d, s = 0):
        self.path = p
        self.name = n
        self.isDir = d
        self.__size__ = s
        self.timestamp = datetime.now()

    def GetFilePath(self):
        """Get the path of this file"""
        return self.path

    def GetFuturePath(self):
        """Get the path if it was a current folder"""
        return self.path + self.name + "\\"

    def GetDirString(self, parent = False):
        """Gets the string in the \"DIR\" format"""
        dateStr = f"{self.timestamp.day:0>2}/{self.timestamp.month:0>2}/{self.timestamp.year:0>4}"
        timeStr = f"{self.timestamp.hour:0>2}:{self.timestamp.minute:0>2}"
        if (self.isDir):
            if (parent):
                name = ".."
            else:
                name = self.name
            return f'{dateStr} {timeStr} {"<DIR>":12} {name}'
        return f"{dateStr} {timeStr} {self.__size__:12} {self.name}"

class Directory(MainFileClass):
    """A simple folder
    Can contain file and other folder"""
    
    def __init__(self, p, n, par = None, dt = datetime.now()):
        self.parent = par
        self.path = p
        self.name = n
        self.isDir = True
        self.size = 0
        self.content = {}
        if (self.parent != None):
            self.content[".."] = self.parent
        self.timestamp = dt
        self.counter = -1
    
    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if (self.counter >= len(self.content)):
            raise StopIteration
        return self.content[list(self.content.keys())[self.counter]]
    

    def AddDir(self, name):
        """Add a folder to this folder
        
        returns the created folder"""
        self.content[name] = Directory(self.GetFuturePath(), name, self)
        return self.content[name]
    
    def RemoveDir(self, name):
        """Removes a folder from this folder"""
        del self.content[name]

    def AddContent(self, content):
        """Add a specific file to this folder
        
        returns the file"""
        self.content[content.name] = content
        return self.content[content.name]

    def GetDirContent(self):
        """Types the content of the dir on the shell"""
        print(f"Showing DIR for path \"{self.GetFuturePath()}\"")
        for file in self:
            if (file == self.parent):
                print(file.GetDirString(True))
            else:
                print(file.GetDirString())

class Disk(Directory):
    """A disk
    Works like a directory but with extra stuff"""
    
    def __init__(self, n, fulln, sn, dt = datetime.now()):
        self.path = ""
        self.name = n
        self.fullName = fulln
        self.isDir = True
        self.size = 0
        self.content = {}
        self.timestamp = dt
        self.counter = -1
        self.serialNumber = sn
    
    def GetDiskInfo(self):
        """Returns the disk info"""
        return f"Disk \"{self.fullName}\" ({self.name})\nSerial number : {self.serialNumber}"
    
    def GetDirContent(self):
        """Types the content of the disk on the shell"""
        print(self.GetDiskInfo())
        for file in self:
            print(file.GetDirString())

class File(MainFileClass):
    """A simple file
    Used as a parent class for other filetype"""

    def __init__(self, p, n, s, dt = datetime.now()):
        self.path = p
        self.name = n
        self.isDir = False
        self.__size__ = s
        self.timestamp = dt
    
    def PutFileOnDir(self, direct):
        """Put this file on a folder
        
        returns this file"""
        direct.AddContent(self)
        self.path = direct.GetFuturePath()
        return self

class TextFile(File):
    """A simple text file
    Contains text"""
    
    def __init__(self, p, n, c = "", s = 0, dt = datetime.now()):
        self.path = p
        self.name = n
        self.isDir = False
        self.content = c
        self.timestamp = dt
        self.__size__ = 0
        self.RecalculateSize()

    def RecalculateSize(self):
        """Only calculate the file size"""
        self.__size__ = len(self.content)

    def UpdateContent(self, c):
        """Updates the content and recalculate the file size"""
        self.content = c
        self.RecalculateSize()

    def TypeContent(self):
        """Types the content to the shell"""
        print(f"Content of {self.name} :\n{self.content}")
 
if __name__ == "__main__":
    print("Running debug on \"component.py\"\n")
    DiskA = Directory("","A:")
    UserDir = DiskA.AddDir("USERS")
    ProgDir = DiskA.AddDir("PROGRAMS")
    UserDir.AddDir("TEST")
    FoxyFile = TextFile("","FOXY.TXT", "Is mayonnaise an instrument ?")
    FoxyFile.PutFileOnDir(UserDir)
    TextFile("","GUIGUI.TXT", "YOU SHOULD GET CORRUPTED NOW").PutFileOnDir(UserDir)
    TextFile("","ALEX.TXT", "gay sex.").PutFileOnDir(UserDir)
    TextFile("","LOUVTT.TXT", "Idk what's going on here and at this point i'm too afraid to ask").PutFileOnDir(UserDir)
    
    DiskA.GetDirContent()
    print()
    UserDir.GetDirContent()
    print()
    for file in UserDir:
        if (type(file) == TextFile):
            file.TypeContent()
            print()
