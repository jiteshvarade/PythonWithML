
class Demo:
    Data1 = 11 # class variable  # same for all objects
    Data2 = 22 # class variable 

    def __init__(self, A, B):
        print("Inside constructor")
        self.No1 = A  # instance variable # different for different objects
        self.No2 = B  # instance variable    

if __name__ == "__main__":
    obj1 = Demo(5,10)
    obj2 = Demo(15,20)

    print("Value of No1 from obj1 : ",obj1.No1)
    print("Value of No2 from obj1 : ",obj1.No2)

    print("Value of No2 from obj2 : ",obj2.No1)
    print("Value of No2 from obj2 : ",obj2.No2)

    print("Value of Data1 : ",Demo.Data1)
    print("Value if Data2 : ",Demo.Data2) 