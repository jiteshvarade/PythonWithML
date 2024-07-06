
EvenOdd = lambda a : a % 2 == 0

if __name__ == "__main__":
    No = int(input("Enter a number : "))
    Result = EvenOdd(No)
    if(Result):
        print("Number is even")
    else:
        print("Number is odd")

    