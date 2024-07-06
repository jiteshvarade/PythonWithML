

def Addition(List):
    Ans = 0
    for i in range(len(List)):
        Ans = Ans + List[i]
    return Ans

def main():
    Size = int(input("Enter the number of elements : "))
    List = list()

    for i in range(Size):
        # a = int(input())
        List.append(int(input()))

    Ret = Addition(List)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()