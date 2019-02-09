# We decode bytes and encode strings, (DB and ES)
import sys

script = "ex23.py" # input("Name of the script: ")
input_encoding = "utf-8" # input("Input encoding: ")
error = "strict" # input("Type of error: ")


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # We decode bytes and encode strings

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
