
# function passed to Filter must return true or false
def FilterJ(function ,list):
    Result = []
    for i in range(len(list)):
        if(function(list[i])):
            Result.append(list[i])
    return Result


# one input one return
def MapJ(function, list):
    Result = []
    for i in range(len(list)):
        a = function(list[i])
        Result.append(a)
    return Result

# two parameter on return
def ReduceJ(fucntion, list):
    Result = 0
    for i in range(len(list)):
        Result = fucntion(Result, list[i])
    return Result

