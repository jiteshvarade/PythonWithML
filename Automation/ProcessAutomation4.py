import psutil
import time
import schedule

def CreateLog(FileName = "Marvellous"):
    print("Log file created at : ",time.ctime())
    file_name = FileName+" "+time.ctime()+".log"
    fd = open(file_name, "w")
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
    schedule.every(1).minutes.do(CreateLog)

    while(True):
        schedule.run_pending()
        time.sleep(1)

