# Escape sequences

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishes
\t* Catnip\n\t* Grass
"""
# In the following way we don't need a backslash to print a new line
# But we can also use backslash n if we want to

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)