from functools import reduce

if __name__ == "__main__":
    Data = [11,14,20,23,18,16,15,20]
    print("Original data is : ",Data)
    FData = list(filter(lambda No : No % 2 == 0, Data))
    print("Data after filter operation is : ",FData)
    MData = list(map(lambda No : No + 1, FData))
    print("Data after map operation is : ",MData)
    RData = reduce(lambda a,b : a + b, MData)
    print("Data after reduce operation is : ",RData)