
def Display(Cnt):

    if(Cnt <= 0):
        print("Invalid Input")
        return
    
    i = 1
    while(i <= Cnt):
        print("Jay Ganesh...")
        i = i + 1

def main():
    Cnt = int(input("Enter the frequency : "))
    Display(Cnt)

if __name__ == "__main__":
    main()