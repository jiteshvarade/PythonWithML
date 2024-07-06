import requests
import datetime
import time
import schedule 

def Schedule_Server():
    print("Scheduler executes after each minute : ",datetime.datetime.now())
    # url = 'https://fitness-server-u793.onrender.com'
    url = "https://devauction.onrender.com"

    for j in range(1,99999999999999999999999999999999999999999):
        for i in range(9999999999999999999):
            response = requests.get(url)

            if response.status_code == 200:
                content = response.text
                print(content)
            else:
                print(f"Request failed. Status code: {response.status_code}")

if __name__ == "__main__":
    # schedule.every(10).minutes.do(Schedule_Server)

    # while(True):
    #     schedule.run_pending()
    #     time.sleep(1)
    Schedule_Server()