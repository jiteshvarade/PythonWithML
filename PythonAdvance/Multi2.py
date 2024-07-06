import os
import multiprocessing

def Task1(No):
    print("Executing first task")
    print("PID of task1 : ",os.getpid())
    print("PPID of task1 : ",os.getppid())

def Task2(No):
    print("Executing first task")
    print("PID of task2 : ",os.getpid())
    print("PPID of task2 : ",os.getppid())

if __name__ == "__main__":
    print("PID of running process : ",os.getpid())
    print("PID of parent process i.e command promt is : ",os.getppid())

    Value = 11
    p1 = multiprocessing.Process(target = Task1, args = (Value, ))
    p2 = multiprocessing.Process(target = Task2, args = (Value, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    