import os
import threading

def Even(No): 
    j = 2
    for i in range(No):
        print("Even : ",j)
        j = j + 2

def Odd(No):
    j = 1
    for i in range(No):
        print("Odd : ",j)
        j = j + 2
    print()

    

if __name__ == "__main__":
    No = int(input("Enter the number : "))

    t1 = threading.Thread(target = Even, args = (No, ))
    t2 = threading.Thread(target = Odd, args = (No, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
