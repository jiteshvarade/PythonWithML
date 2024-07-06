import multiprocessing
import os
import time

def Cube(No):
    Sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No*No*No*No*No*No*No*No)
    return Sum

if __name__ == "__main__":
    starttime = time.time()
    Arr = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000,1300000,1400000]

    Result = []

    # for Value in Arr:
    #     Result.append(Cube(Value))

    p = multiprocessing.Pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()

    endtime = time.time()
    print("Time required for execution : ", endtime - starttime)

    print(Result)
