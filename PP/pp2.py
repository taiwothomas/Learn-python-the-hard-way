import sys
script, input_encoding, error = sys.argv

#argument importing and handling
# define the main function of this script. this is where each line of the languages file is taken and returned until there are not more lines (the if statement does this)

def main(language_file, encoding, errors):
  line = language_file.readline()
  line = line.encode('utf-8', errors =errors)
  
#this carries out the subsequent commands as long as the line varaible is not empty. it runs print_line and returns the main function
  
  if line:
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)

#print_line is defined here. this is where the line variable is striped of the \n at the end of each line. then the DBES is applied - decode bytes, encode string. raw_bytes encodes each line of the language file that has been stripped and cooked_string decodes raw_bytes - DBES.
    
def print_line(line, encoding, errors):
  next_lang = line.strip()
  cooked_string = next_lang.decode(encoding, errors=errors)
  raw_bytes = cooked_string.encode(encoding, errors=errors)
  
  
#here the output is structured encoded string (raw_bytes), decoded bytes (cooked_string), separated by a double arrow
  
  print(raw_bytes, "<===>", cooked_string)

#then that languages file object is assigned to a "languages" variable with the proper encoding

languages = open("languages.txt", encoding="utf-8")

# finally the main function is ran 

main(languages, input_encoding, error)