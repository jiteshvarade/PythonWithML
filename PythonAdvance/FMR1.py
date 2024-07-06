from functools import reduce

def ChkEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(No1, No2):
    return No1 + No2

if __name__ == "__main__":
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list : ",Data)
    # filter(Name_of_function, Name_of_Variable)
    FData = list(filter(ChkEven,Data))
    print("Data after filter activity : ",FData)
    MData = list(map(Increase, FData))
    print("Data after map activity : ", MData)
    RData = reduce(Add, MData)
    print("Data after reduce activity is : ",RData)
