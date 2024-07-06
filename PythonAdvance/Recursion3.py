

def fun(i):
    print("Inside fun ", i)
    i = i + 1
    fun(i)

if __name__ == "__main__":
    fun(1)

# sys.getrecursionlimit() gives value 1000 here