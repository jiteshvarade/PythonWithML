import os
from time import sleep

def Clock():
    for i in range(24):
        for j in range(60):
            for k in range(60):
                print(i,":",j,":",k)
                sleep(1)
                os.system("clear")

if __name__ == "__main__":
    Clock()