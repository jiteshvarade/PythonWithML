from Marvellous import *

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Sum = Addition(No1,No2)
    print("Addition is : ",Sum)

    Diff = Substraction(No1, No2)
    print("Substraction is : ",Diff)

    Mul = Multiplication(No1,No2)
    print("Multiplication is : ",Mul)

    Div = Division(No1,No2)
    print("Division is : ",Div)

main()