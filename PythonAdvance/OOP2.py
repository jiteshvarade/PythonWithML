
class Demo:
    Data1 = 11 # class variable  # same for all objects
    Data2 = 22 # class variable 

    def __init__(self, A, B):
        print("Inside constructor")
        self.No1 = A  # instance variable # different for different objects
        self.No2 = B  # instance variable    

    @classmethod
    def Fun(cls): # class methode
        print("Value of Data1 from fun : ",Demo.Data1)
        print("Value of Data2 from fun : ",Demo.Data2)

    @staticmethod
    def gun():
        print("Inside static methode")

if __name__ == "__main__":
    Demo.gun()
    Demo.Fun()
    obj1 = Demo(5,10)
    obj2 = Demo(15,20)

    