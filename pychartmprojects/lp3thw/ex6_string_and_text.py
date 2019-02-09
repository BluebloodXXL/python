types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

damn = "damn !"
hilarious = False
joke_evaluation = "{} Isn't that joke so funny ?! {}"
print(joke_evaluation.format(damn, hilarious))


# Using method for that
def joke_evaluation():
    return "{} Isn't that joke so funny ?! {}".format(damn, hilarious)


print("This is from method,", joke_evaluation())

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
