import os

if __name__ == "__main__":
    print("Enter the name of file that you want to open for writing purpose : ")
    Fname = input()

    if(os.path.exists(Fname)):
        fobj = open(Fname, "w")
        print("File is successfully opened in write mode")

        print("Enter data that you want to write in the file")
        Data = input()

        fobj.write(Data)
    else:
        print("Unable to open file as file does not present in the directory")