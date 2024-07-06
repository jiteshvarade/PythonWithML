import os

if __name__ == "__main__":
    print("Enter the name of file that you want to open for readind purpose : ")
    Fname = input()

    if(os.path.exists(Fname)):
        fobj = open(Fname, "r")
        print("File is successfully opened in read mode")

        str1 = fobj.readline()
        str2 = fobj.readline()
        str3 = fobj.readline()
        str4 = fobj.readline()

        print(str1)
        print(str2)
        print(str3)
        print(str4)

        fobj.close()  #releasing resources
    else:
        print("Unable to open file as file does not present in the directory")