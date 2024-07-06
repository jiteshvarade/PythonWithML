
class Arithmetic:
    def __init__(self,i,j):  # __init__ : special variable
        self.No1 = i
        self.No2 = j

    def Addition(self):
        return self.No1+self.No2
    
    def Substraction(self):
        return self.No1-self.No2


if __name__ == "__main__":  # __name__ : special variable
    print("Demonstration of Object Orientation")
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    obj = Arithmetic(No1,No2) # no new keyword to create a object
    
    Ret = obj.Addition()
    print("Addition of numbers : ",Ret)

    Ret = obj.Substraction()
    print("Substraction of numbers : ",Ret)