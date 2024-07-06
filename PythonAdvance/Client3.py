import Marvellous as M

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Sum = M.Addition(No1,No2)
    print("Addition is : ",Sum)

    Diff = M.Substraction(No1, No2)
    print("Substraction is : ",Diff)

    Mul = M.Multiplication(No1,No2)
    print("Multiplication is : ",Mul)

    Div = M.Division(No1,No2)
    print("Division is : ",Div)

main()