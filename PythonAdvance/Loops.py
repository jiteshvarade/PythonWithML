#Demonstrations of for and while loops   

def DisplayF():
    for i in range(5):
        print(i+1)

def DisplayW():
    i = 1
    while(i <= 5):
        print(i)
        i = i+1

def main():
    DisplayF()
    DisplayW()

if __name__ == "__main__":
    main()