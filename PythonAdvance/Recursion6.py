i = 1

def DisplayR():
    global i
    if(i > 10):
        return
    print("Inside DisplayR function : ",i)
    i = i + 1
    DisplayR()

if __name__ == "__main__":
    DisplayR()