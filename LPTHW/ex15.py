from sys import argv
#take two argument variables - script and filename
script, filename = argv
#txt variable defined to open the file called in argument filename
txt = open(filename)
#print the name of the file and print the file using read function on variable txt which contains the file
print(f"Here's your {filename} file.")
print(txt.read())
#print a preprompt of a variable that collects the filename
print("Type the filename again:")
file_again = input("> ")
#set a variable to open the file (create the file object) using the filename variable in the previous line
txt_again = open(file_again)
#print the above variable, which contains the file, with read
print(txt_again.read())