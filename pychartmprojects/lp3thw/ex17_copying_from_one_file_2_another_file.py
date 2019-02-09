from os.path import exists

from_file = input("contents will be copied from the following file: ")
to_file = input("contents will be copied to the following file: ")

print(f"Copying from the {from_file} to {to_file}")

sourceFile = open(from_file, 'r')
sourceData = sourceFile.read()

print(f"The source file is {len(sourceData)} bytes long.")

print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit Return to continue, CTRL-C to abort.")
input()

outFile = open(to_file, 'w+')
outFile.write(sourceData)

outFile.close()
sourceFile.close()