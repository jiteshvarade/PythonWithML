
def Divsion(a,b):
    try:
        Ans = a/b
    except Exception as err:
        print("Error :",err)
    else:
        print("Divsion of number is : ",Ans)
    finally:
        print("Always executed")
    

if __name__ == "__main__":
    No1 = input("Enter first number : ")
    No2 = input("Enter second number : ")
    Divsion(No1,No2)
    