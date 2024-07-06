# List

# List is ordered
# List is indexed
# List is mutable
# List allows duplicate elements

if __name__ == "__main__":
    Arr1 = [100, 20 ,30, 40, 50]  # square bracket indicates list
    Arr2 = ["Marvellous", 30, True, 45.4]  # List can store hetrogeneous data
    print(type(Arr1), type(Arr2))   # < type list >
    print(Arr1[0], Arr2[2])     # List is indexed
    Arr1[0] = 200   # Data is mutable inside list
    print(Arr1[0])  
    Arr1.append(51) # List is mutable
    print(Arr1[5])
    print(len(Arr1)) 
