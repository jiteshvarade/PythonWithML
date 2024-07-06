import datetime
import time
import schedule 

def Schedule_Minute():
    print("Scheduler executes after each minute : ",datetime.datetime.now())

def Schedule_Hour():
    print("Scheduler executes after each Hour : ",datetime.datetime.now())

def Schedule_Sunday():
    print("Scheduler executes after each Sunday : ",datetime.datetime.now())

if __name__ == "__main__":
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)
    schedule.every(1).hour.do(Schedule_Hour)
    schedule.every(1).sunday.do(Schedule_Sunday)

    while(True):
        schedule.run_pending()
        time.sleep(1)