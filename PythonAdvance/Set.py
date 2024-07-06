# Set dataype

# Unordered
# Unindexed
# hetrogeneous data
# duplicate not allowed
# mutable

Arr = {11, 18, 90, True, "Marvellous", 11}
print(type(Arr))
print(len(Arr))
print(Arr)

# cannot access set elements using indexing because set is unordered and unindexed
# print(Arr[0])

Arr.add("Python")
print(Arr)

Arr.discard("Python")
print(Arr)

Arr.remove(11)
print(Arr)