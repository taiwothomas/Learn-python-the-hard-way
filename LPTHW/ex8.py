formatter = "{} {} {} {}"

#the formatter variable is a string variable that takes four arguments
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter,formatter))
print(formatter.format(
  "Forever thus the trend of progress flows\n", 
  "Unfettered lawless sprits strive in vain\n",
  "Perfections crystal summit to attain\n",
  "He that must be great must his own ruler be"
))