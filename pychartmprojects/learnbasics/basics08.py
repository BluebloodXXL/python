# Open a file
file = open('basics08.txt', 'w')

# Get file info
print('Name:', file.name)
print('Is closed ?', file.closed)
print('Opening mode', file.mode)

# Writing in the opend file
file.write('I love Python ')
file.write('and Javascript')

# Closing file
file.close()

# Once the file is opened in 'w' mode,
# Until we close the file the write function will continue to append

# But once we close the file and again open it in 'w' mode and use the write function
# Then no more it will append but overwrite the existing records
# file = open('basics08.txt', 'w')
# file.write('I love Dart ')
# file.write('and also Flutter')
# file.close()

# Append, to append we have to open the file in append mode
file = open('basics08.txt', 'a')
file.write(' \nand I love Dart ')
file.write('and Flutter')
file.close()

# This is Super Kool we can add new line even to the file while writing and appending
# with our good old back slash n

# Read from a file, open it with r+
file = open('basics08.txt', 'r+')
fileText = file.read(100)
print('The text below is from our file ' + file.name + ',\n' + fileText)
file.close()

# Create new file with w+ mode and do all other things
file = open('basics08_from_PYTHON.txt', 'w+')
file.write('I love Dart ')
file.write('and also Flutter')
file.close()

file = open('basics08_from_PYTHON.txt', 'r+')
fileText = file.read(100)
print('The text below is from our file ' + file.name + ',\n' + fileText)
file.close()