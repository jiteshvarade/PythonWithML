
def Area(R, Pi = 3.14):
    return R*Pi*Pi

if (__name__ == "__main__"):
    R = int(input("Enter the radius : "))
    Ans = Area(R)
    print("Area is : ",Ans)