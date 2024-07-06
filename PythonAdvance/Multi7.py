import os
import threading

def Even(No):
    print("PID of even process : ",os.getpid())
    print("TID of even thread : ", threading.get_ident())
    j = 2
    for i in range(No):
        print(j, end=" ")
        j = j + 2

def Odd(No):
    print("PID of odd process : ",os.getpid())
    print("TID of odd thread : ", threading.get_ident())
    j = 1
    for i in range(No):
        print(j, end=" ")
        j = j + 2
    print()

    

if __name__ == "__main__":
    No = int(input("Enter the number : "))

    print("TID of main thread : ", threading.get_ident())
    print("PID of even process : ",os.getpid())

    t1 = threading.Thread(target = Even, args = (No, ))
    t2 = threading.Thread(target = Odd, args = (No, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of maain porcess : ")
