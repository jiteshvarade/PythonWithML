import os

if __name__ == "__main__":
    print("Enter the name of file that you want to create : ")
    Fname = input()

    if(os.path.exists(Fname)):
        print("Unable to create file as file already existing")
    else:
        open(Fname, "x")
        print("File gets successfully created")