import sys

def Addition(arr):
    Ans = 0
    for i in range(1,len(arr)):
        Ans = Ans + int(arr[i])       
    return Ans

def main():
    print("Addition programm using commnd line arguments")

    if(len(sys.argv) < 3):
        print("Atleast provide 2 commnd line arguments")
        return

    Result = Addition(sys.argv)
    print("Addition is : ",Result)

if __name__ == "__main__":
    main()