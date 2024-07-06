
def Display(Cnt):

    if(Cnt <= 0):
        print("Invalid Input")
        return
    
    for i in range(Cnt):
        print("Jay Ganesh...", end="")

def main():
    Cnt = int(input("Enter the frequency : "))
    Display(Cnt)

if __name__ == "__main__":
    main()