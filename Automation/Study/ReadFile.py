import os

if __name__ == "__main__":
    print("Enter the name of file that you want to open for readind purpose : ")
    Fname = input()

    if(os.path.exists(Fname)):
        fobj = open(Fname, "r")
        print("File is successfully opened in read mode")

        Data = fobj.read(5)

        print(Data)

        fobj.close()  #releasing resources
    else:
        print("Unable to open file as file does not present in the directory")