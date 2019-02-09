# Functions baby
# First to define a function we need to use the keyword def

# Defining simple function without parameter
def sayHello():
    print('Hello World')


# Calling the simple function
sayHello()


# Defining simple function with parameter
def sayHello(name):
    print('Hello ', name)


# Calling the simple function with parameter
sayHello('Mahir')


# DEFAULT ARGUMENT: Defining function with default argument
def sayHello(name='DEFAULT_NAME'):
    print('Hello ', name)


sayHello()
sayHello('Mahir')  # if parameter is given default argument will be overwritten


# Let's now return
def add2(num1=1, num2=1):
    # if decided to set default value then default value should be set to all parameters, won't work otherwise
    return num1 + num2


print(add2(2, 2))
print(add2())

# int float string are immutable because of call by value
numX = 3


def altNum(num):
    num = num + 1
    print(num, 'Printing from inside after changing')
    return


altNum(numX)
print(numX, 'Printing from outside after changing')


# Other structured data types are mutable such as List, Dictionary because of pass by value
def add2List(myList):
    myList.append(4)
    print('Value inside function ', myList)
    return


myList = [1, 2, 3]
add2List(myList)
print('Value outside function ', myList)
