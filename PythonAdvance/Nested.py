def Calculations(No1, No2):
    def Addition(X, Y):
        return X+Y
    def Substraction(X, Y):
        return X-Y
    Ans1 = Addition(No1, No2)
    Ans2 = Substraction(No1, No2)
    return Ans1, Ans2

A = int(input("Enter first number : "))
B = int(input("Enter the second number : "))

Addition, Subtraction = Calculations(A, B)

print("Addition is : ",Addition)
print("Subtraction is : ",Subtraction)