import multiprocessing
import os

def Cube(No):
    print("PID is : ",os.getpid())
    return No*No*No

if __name__ == "__main__":
    Arr = [10,20,30,40,50]
    Result = []

    # for Value in Arr:
    #     Result.append(Cube(Value))

    p = multiprocessing.Pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()

    print(Result)
