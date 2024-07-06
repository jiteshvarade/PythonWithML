from functools import reduce

def EvenChk(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 2

def Add(a,b):
    return a+b

if __name__ == "__main__":
    print("----Demonstration of Filter Map Reduce")
    #Demonstration of Filter, Map, Reduce using normal functions

    arr = [8,9,5,16,2,4,21,30,11]
    evenArr = list(filter(EvenChk,arr))
    print("Data after filter ",evenArr)
    ModArray = list(map(Increase, evenArr))
    print("Data after map",ModArray)
    sum = reduce(Add, ModArray)
    print("Addition of even numbers ",sum)

    #Demonstration of Filter, Map, Reduce using lambda function

    evenArr = list(filter(lambda No : (No % 2 == 0), arr))
    print("Data after filter using lambda ",evenArr)
    ModArr = list(map(lambda No : No + 2, evenArr))
    print("Data after map using lambda ", ModArr)
    sum = reduce(lambda a,b : a+b, ModArray)
    print("Addition of even numbers using lambda ",sum)

    