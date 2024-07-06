i = 1

def fun():
    global i
    if(i > 10):
        return
    print("Inside fun ", i)
    i = i + 1
    fun()

if __name__ == "__main__":
    fun()
