def Calculations(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    return Add,Sub

A = int(input("Enter first number : "))
B = int(input("Enter the second number : "))

Addition, Subtraction = Calculations(A, B)

print("Addition is : ",Addition)
print("Subtraction is : ",Subtraction)