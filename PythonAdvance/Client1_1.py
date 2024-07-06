from Marvellous import Addition, Multiplication

def main():

    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Sum = Addition(No1,No2)
    print("Addition is : ",Sum)

    Mul = Multiplication(No1,No2)
    print("Multiplication is : ",Mul)

main()