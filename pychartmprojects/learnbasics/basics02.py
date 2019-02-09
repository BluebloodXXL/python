# Variables and datatypes
# You don't need semicolon in python
# Python is not strictly typed

# String Concatenation
my = 'Hello'
space = ' '
msg = my + space + 'World'
print(msg)

# Without type hint
variable01 = 'Hello World'
variable02 = 55


# With type hint
variable_01: str = 'Hello World'
variable_02: int = 98
variable_03: float = 4.4
variable_04: object = object

# Commonly used structured data types, list, dictionary

# Lists are like normal arrays
myList = [1,2,3, 'Not a Number']
print(myList)
print(myList[2])
print(myList[3])

# Dictionaries are like associative arrays within curly braces, keys and values
myDict = {'House': 47, 'Road': 5}
print(myDict)
print(myDict['Road'])

# Flushing Datatypes using type method
print(type(myDict))
print(type(myList))

