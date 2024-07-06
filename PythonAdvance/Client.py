import Marvellous

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Sum = Marvellous.Addition(No1,No2)
    print("Addition is : ",Sum)

    Diff = Marvellous.Substraction(No1, No2)
    print("Substraction is : ",Diff)

    Mul = Marvellous.Multiplication(No1,No2)
    print("Multiplication is : ",Mul)

    Div = Marvellous.Division(No1,No2)
    print("Division is : ",Div)

main()