# String Functions

myStr = 'Hello World ?'

# Capitalize
print(myStr.capitalize())

# Swap Case
print(myStr.swapcase())

# Uppercase
print(myStr.upper())

# Lowercase
print(myStr.lower())

# Get Length
print(myStr.__len__()) # or, print(len(myStr)) would work too

# Replace
print(myStr.replace('World', 'Everyone'))

# Count substring occurence
print(myStr.count('o'))

# starts with
print(myStr.startswith('H'))

# Ends with
print(myStr.endswith('?'))

# Split string into words
print(myStr.split())

# Count number of words in a sentence
sentence = 'This is going to be awsome'
print('Number of words in', '"'+sentence+'"', 'is', len(sentence.split()))

# Find function to find the position of substring
print('The given substring starts at,', sentence.find('to'))