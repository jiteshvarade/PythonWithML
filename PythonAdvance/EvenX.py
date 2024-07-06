def ChkEven(No):
    if((No % 2) == 0):
        print("Number is even")
    else:
        print("Number is odd")

def main():
    print("Enter the number : ")
    A = int(input())

    ChkEven(A)

# print(__name__)
# Starter
if __name__ == "__main__":
    main()