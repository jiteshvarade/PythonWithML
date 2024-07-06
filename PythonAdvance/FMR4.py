
# User defined module which contains user defined Filter, Map, Reduce functions
import JTools

ChkEven = lambda No : (No % 2 == 0)

Increase = lambda No : No + 1

Add = lambda No1, No2 : No1 + No2

if __name__ == "__main__":
    print("Enter size of list : ", end=" ")
    Size = int(input())
    print("Enter elements inside array : ")
    list = []
    for i in range(Size):
        No = int(input())
        list.append(No)
    
    FData = JTools.FilterJ(ChkEven, list)
    print("Data after filter operation is : ",FData)
    MData = JTools.MapJ(Increase, FData)
    print("Data after map operation is : ",MData)
    RData = JTools.ReduceJ(Add, MData)
    print("Sum of elements is : ", RData)