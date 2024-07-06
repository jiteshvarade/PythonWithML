import os

if __name__ == "__main__":
    print("Enter the name of directory that you want to scan")
    Dname = input()

    print("List of files in directory are : ")
    for foldername, subfoldername, filenames in os.walk(Dname):
        for fname in filenames:
            print(fname)