

def Display(List):
    for i in range(len(List)):
        print(List[i])


def main():
    Size = int(input("Enter the number of elements : "))
    List = list()

    for i in range(Size):
        # a = int(input())
        List.append(int(input()))

    Display(List)

if __name__ == "__main__":
    main()