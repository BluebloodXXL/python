# Conditionals
# Indent is very important
# Break the indent to get out of the scope

color = 'yellow'
x = 1

# Simple if
if not x > 1:
    print('X is ok')

# Simple if else
if x == 1:
    print('x is one')
else:
    print('x is not one')

# Simple if else elif
if color == 'red':
    print('color is red')
elif color == 'blue':
    print('color is blue')
else:
    print('color is nither red or blue')

# Nested if
if color == 'yellow':
    if x == 1:
        print('Every thing is fine')

# Joining two Nested if
if color == 'yellow' and x == 1:
    print('Every thing is Joined')
