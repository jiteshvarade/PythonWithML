
def Cube(No):
    return No*No*No

if __name__ == "__main__":
    Arr = [10,20,30,40,50]
    Result = []

    for Value in Arr:
        Result.append(Cube(Value))

    print(Result)
