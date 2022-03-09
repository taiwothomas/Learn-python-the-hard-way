from sys import argv
#script takes two arguments - script and input_file
script, input_file = argv
# write a print all function that prints the object after opening it
def print_all(f):
  print(f.read())
# write a rewind function that returns the object to the start using seek
def rewind(f):
  f.seek(0)
# write a print_a_line function that print a specific line of an object using readline which loads one line of a file
def print_a_line(line_count, f):
  print(line_count, f.readline())
# store a variable that holds the file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# use the defined rewind function to take the open file to the start
rewind(current_file)

print("Let's print three lines:")
# set current line as 1
current_line = 1 
# use defined print_a_line function to print the first line of the file with the line number
print_a_line(current_line, current_file)
# increase the count of the current_line variable
current_line = current_line + 1
# use print_a_line to print the second line with the line number
print_a_line(current_line, current_file)
# increase the count of current_line and use print_a_line to print the third line of the file
current_line = current_line + 1
print_a_line(current_line, current_file)

#subsequent calling readline function reads subsequent lines. that's why we need the seek function to take us back to zero.