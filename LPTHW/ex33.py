def top_bottom(bottom):
  
  i = 0
  numbers = []

  while i < bottom:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


  print("The numbers: ")

  for num in numbers:
    print(num)

print('How long is your list? ')
bottom = int(input())
top_bottom(bottom)