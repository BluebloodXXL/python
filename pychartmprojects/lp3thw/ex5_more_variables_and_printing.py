# You also must start the string with the letter f for “format,”
# as in f"Hello {somevar}". This little f before the " (double-quote)
# and the {} characters tell Python 3, “Hey, this string needs to be formatted.
# Put these variables in there

my_name = 'Mahir Chowdhury'
my_age = 24 # not a lie
my_height = 4.11 # inches
my_weight = 65 # kilo
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} feet tall.")
print("Actually it's not even tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually it's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
# We are going to round our float
print(f"If I add {my_age}, {my_height} and {my_weight} I get {round(total)} after rounding.")
