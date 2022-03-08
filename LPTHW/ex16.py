from sys import argv
#take two arguments for the function
script, filename = argv
# print a bunch of instructions including one where the filename argument value is displayed
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#request for an input before proceeding with the script. the return input just continues the script on the next line
input("?")
#some narrative then a variable contain the file object using the open function
print("Opening the file...")
target = open(filename, 'w')
#narrative then truncate function on the variable to erase the content of its file object
print("Truncating the file. Goodbye!")
target.truncate()
#narrative
print("Now I'm going to ask you for three lines.")
#input variable for the file object
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#narrative
print("I'm going to write these to the file.")
#writing content into the file object contained in the "target" variable using the write funtion
target.write(f"{line1}\n{line2}\n{line3}\n")

#narrative and then closing the file object using the close function on the "target" variable
print("And finally we close it.")
target.close()