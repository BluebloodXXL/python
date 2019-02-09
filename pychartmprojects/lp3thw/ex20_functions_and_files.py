input_file = input("Please give us the name of the file: ")


def print_all(file):
    file_data = file.read()
    print(file_data)


def rewind(file):
    file.seek(0)


def print_a_line(line_count, file):
    print(line_count, file.readline())


def call_print_line(line):
    current_line = line
    print_a_line(current_line, current_file)


current_file = open(input_file, 'r')

print("First let's print the whole file: \n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines: \n")


for i in range(1, 3+1, 1):
    call_print_line(i)

