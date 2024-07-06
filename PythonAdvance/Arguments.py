# Types of function arguments

# 1. Positional arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable number of arguments

def Information(Name, Age, Salary = 1000000):
    print("Name is : ",Name)
    print("Age is : ", Age)
    print("Salary is : ",Salary)

if (__name__ == "__main__"):
    Information("Amit", 32, 90000)
    Information("Pooja", 29, 70000)
    Information("James", 20)
    Information(Age = 31, Salary = 80000, Name = "Sagar")