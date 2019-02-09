# single line comment
'''
Multiline comment
'''

print('This is going to be printed within single quote')

print("This is going to be printed within double quote")

print('''We need triple quote for multiple line printing, here single and double quote will not work
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap 
into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the 
release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
software like Aldus PageMaker including versions of Lorem Ipsum.''')

# Print substrings with specific possition
print('Substring printing'[0])

# Print substrings with range from 4th position up to 7th position, 4th,5th,6th will be printed
print('Substring printing'[4:7])

# For printing a number we don't need any quote
print(3)

# Printing multiple things in a same line, use comma
print(1,2,3, "Joyan's friend")

# New line, our old friend backslash n
print('Line 01\nLine 02\nLine 03\n')

# Avoiding escape
print(r'C:\\somewhat directory')