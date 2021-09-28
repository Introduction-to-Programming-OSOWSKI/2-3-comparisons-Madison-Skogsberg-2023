#WRITE YOUR CODE IN THIS FILE
#define function
#add parameters
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False
#define function
#add parameters
def lessThan(x, y):
    if x < y:
        return True
    else:
        return False
#define function
#add parameters
def equalTo(x, y):
    if x == y:
        return True
    else:
        return False
#define function
#add parameters
def greaterOrEqual(x, y):
    if x > y:
        return True
    elif x == y:
        return True
    else:
        return False
#define function
#add parameters
def lessOrEqual(x, y):
    if x < y:
        return True
    elif x == y:
        return True
    else:
        return False
#run all functions
print(greaterThan(10, 11))
print(lessThan(10, 11))
print(equalTo(10,11))
print(greaterOrEqual(10,11))
print(lessOrEqual(10, 11))