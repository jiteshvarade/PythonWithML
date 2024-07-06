
def ChkEven(No):
    return (No % 2 == 0)

def Increase(No):
    return No + 1

def Add(No1, No2):
    return No1 + No2

# function passed to Filter must return true or false
def FilterJ(function ,list):
    Result = []
    for i in range(len(list)):
        if(function(list[i])):
            Result.append(list[i])
    return Result


# one input one return
def MapJ(function, list):
    Result = []
    for i in range(len(list)):
        a = function(list[i])
        Result.append(a)
    return Result

# two parameter on return
def ReduceJ(fucntion, list):
    sum = 0
    for i in range(len(list)):
        sum = fucntion(sum, list[i])
    return sum

if __name__ == "__main__":
    print("Enter size of list : ", end=" ")
    Size = int(input())
    print("Enter elements inside array : ")
    list = []
    for i in range(Size):
        No = int(input())
        list.append(No)
    
    FData = FilterJ(ChkEven, list)
    print("Data after filter operation is : ",FData)
    MData = MapJ(Increase, FData)
    print("Data after map operation is : ",MData)
    RData = ReduceJ(Add, MData)
    print("Sum of elements is : ", RData)