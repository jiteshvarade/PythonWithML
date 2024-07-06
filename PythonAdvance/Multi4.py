import multiprocessing

def Even(No):
    j = 2
    for i in range(No):
        print(j, end=" ")
        j = j + 2

def Odd(No):
    j = 1
    for i in range(No):
        print(j, end=" ")
        j = j + 2
    print()

    

if __name__ == "__main__":
    No = int(input("Enter the number : "))

    p1 = multiprocessing.Process(target = Even, args = (No, ))
    p2 = multiprocessing.Process(target = Odd, args = (No, ))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print("End of maain porcess : ")
