import datetime
import time
import schedule 

def Schedule_Minute():
    print("Scheduler executes after each minute : ",datetime.datetime.now())

if __name__ == "__main__":
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Schedule_Minute)

    while(True):
        schedule.run_pending()
        time.sleep(1)