
def Divsion(a,b):
    Ans = 0
    try:
        Ans = int(a)/int(b)
    except Exception as err:
        print("Error :",err)
    else:
        print("Divsion of number is : ",Ans)
    finally:
        print("Always executed")
    

if __name__ == "__main__":

    try:
        No1 = int(input("Enter first number : "))
        No2 = int(input("Enter second number : "))
        Divsion(No1,No2)
    except Exception as err:
        print("Error :",err)
    
    