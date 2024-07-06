
def Addition(No1, No2):
    return No1+No2

def Substraction(No1, No2):
    return No1-No2

if __name__ == "__main__":
    print("Demonstration of scripting : ")
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Sum = Addition(No1,No2)
    Diff = Substraction(No1,No2)

    print("Addition  of two number is : ",Sum)
    print("Substraction of two numbers is : ",Diff)