def Addition(No1, No2):         #dukan
    print("Inside addition fucntion")
    Ans = 0
    Ans = No1 + No2
    return Ans

def main():                 #ghar
    print("Inside main fucntion")
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))
    Result = Addition(A, B)
    print("Addition is : ",Result)

main()
print("End of application")