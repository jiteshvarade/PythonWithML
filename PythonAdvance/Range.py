# range(start, end, displacement)

# start is by default 0 if not mentioned
# displacement is by default 1 if not mentioned
# end should be mentioned explicitelly (It gets excluded)

def main():
    Arr = range(5) # Arr is treated as object of range type
    print(Arr)
    print(range(5))
    Arr = list(range(5))
    print(Arr)

    print(list(range(8,2,-1)))

if (__name__ == "__main__"):
    main()