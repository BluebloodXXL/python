# Loops

# ForEach loop like javascript and php
people = ['John', 'Sara', 'Kevin']
for person in people:
    print('Current Person: ', person)

# Iterate by sequence index
num_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(1, 7, 2): # Try to understand buddy
    print('Current Alphabet', num_array[i])

# While Loop, So beloved.......
count = 0
while count <= 10:
    count = count + 1
    if count == 2:
        continue # Continue will negate all up coming statements not only the next single one, use it with caution
    print(count)
    if count == 9:
        break


