
def Addition(*No):
    print(type(No))
    print(len(No))
    Ans = 0
    for i in No:
        Ans = Ans + i

    return Ans

if __name__ == "__main__" : 
    Result = Addition(10, 20, 30, 40)
    print("Addition is : ",Result)
