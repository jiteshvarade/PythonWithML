
Add = lambda No1,No2 : No1+No2 # function object : Add
Sub = lambda No1,No2 : No1-No2 # function object : Sub

print("Demonstration of functional : ")
No1 = int(input("Enter first number : "))
No2 = int(input("Enter second number : "))

Sum = Add(No1,No2)
Diff = Sub(No1,No2)

print("Addition  of two number is : ",Sum)
print("Substraction of two numbers is : ",Diff)