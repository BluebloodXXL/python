# Taking INPUT
# If we use end=' ', the input will be taken in the same line
# If we use \n then the input will be taken in the next line
'''
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
'''

x = 2
y = 4.57463456

print("What are you giving me int or float ?", end=' ')

choice = input()
if choice == 'int':
    given = int(input('Please input: '))
elif choice == 'float':
    given = float(input('Please input: '))

if choice == 'int' and given == x:
    check = True
elif choice == 'float' and given == y:
    check = True
else:
    check = False

print(f"You gave me {choice} which is {given} and it is {check}.")
