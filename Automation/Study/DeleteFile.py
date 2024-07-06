import os

if __name__ == "__main__":
    print("Enter the name of file that you want to open for readind purpose : ")
    Fname = input()

    if(os.path.exists(Fname)):
        os.remove(Fname)
    else:
        print("Unable to delete file as file does not present in the directory")