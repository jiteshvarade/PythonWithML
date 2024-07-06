
import sys

if(__name__ == "__main__"):
    print("Recursion limit is : ",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("Recursion limit is : ",sys.getrecursionlimit())
