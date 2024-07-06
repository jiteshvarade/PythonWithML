
def main():
    print("Demonstration of Selection")

    Age = 0

    print("Enter your age : ")
    Age = input()

    if(int(Age) < 18):
        print("Sorry, You are not eligible for voting")
    else:
        print("You can vote")

    print("Thank you for using the application")

if (__name__ == "__main__"):
    main()