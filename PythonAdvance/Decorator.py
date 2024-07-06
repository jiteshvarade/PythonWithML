# predefined function
def sub(A,B):
    print(A - B)

def SmartSub(fptr):
    def Inner(A,B):
        if A < B:
            A,B = B,A
        return fptr(A,B)
    return Inner

sub = SmartSub(sub)

if __name__ == "__main__":
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second numbre : "))

    sub(No1,No2)
