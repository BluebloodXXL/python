print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I'll count the eggs:")
print(3 + 2 + 1 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")

# It gives you directly true or false

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")

# It gives you directly true or false

print("Is it greater?", 5 > -2)

print("Is it greater or equal?", 5 >= -2)

print("Is it less or equal?", 5 <= -2)

print("Is it greater?", 5 > 4.9999999999999999)

# What is the order of operations ?
# In the United States we use an acronym called PEMDAS
# which stands for Parentheses Exponents Multiplication Division
# Addition Subtraction. That’s the order Python follows as well.
# The mistake people make with PEMDAS is to think this is a strict order,
# as in “Do P,then E,then M,then D,then A,then S.” The actual order is
# you do the multiplication and division (M&D) in one step,
# from left to right, then you do the addition and subtraction in one step
# from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).
