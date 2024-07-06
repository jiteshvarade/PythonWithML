import psutil
import time

def CreateLog(FileName = "Marvellous.log"):
    fd = open(FileName, "w")
    seperator = "-"*70

    fd.write(seperator + "\n")
    fd.write("Marvellous Process Log"+"\n")
    fd.write("Log file creted at : "+time.ctime() + "\n")
    fd.write(seperator + "\n")

    Arr = GetProcessInfo()

    fd.write("CONTENTS OF LOG FILE" + "\n")
    fd.write(seperator + "\n")

    for data in Arr:
        fd.write("%s \n" %data)
    
    fd.write(seperator + "\n")

    fd.close()

def GetProcessInfo():
    listprocess = []
    for proc in psutil.process_iter(['pid','name', 'username']):
        listprocess.append(proc.info)
    
    return listprocess

if __name__ == "__main__":
    CreateLog()

