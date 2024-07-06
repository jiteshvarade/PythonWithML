i = 1

def DisplayR():
    global i
    if(i > 10):
        return
    i = i + 1
    DisplayR()
    i = i - 1
    print("Inside DisplayR function : ",i)

if __name__ == "__main__":
    DisplayR()