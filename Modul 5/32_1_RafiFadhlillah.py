the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
  print(f"This is count {number}")

# same as above
for fruit in fruits:
  print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
  print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
  print(f"Adding {i} to the list.")
  # append is a function that lists understand
  elements.append(i)

# now we can print them out too
for i in elements:
  print(f"Element was: {i}")

print(f"data in list:\n{elements}")

#insert into list
while True:
  print("Insert into list? y/n")
  eq = input("> ")
  if eq == "y" or eq == "Y":
    data = int(input("Input data: "))
    index = int(input("In index(0-{}): ".format(len(elements))))
    elements.insert(index, data)
  else:
    break

print(f"data in list:\n{elements}")

#remove data in list
while True:
  print("Remove data in list? y/n")
  rf = input("> ")
  if rf == "y" or eq == "Y":
    data = int(input("Masukan data yang ingin dihapus: "))
    while data in elements:
      elements.remove(data)
    else:
      break
  else:
    break
print(f"data in list:\n{elements}")
#sorted
elements.sort()
print(f"Ascending:\n{elements}")
#reversed
elements.reverse()
print(f"Reverse:\n{elements}")
#frequency with .count()
print("Frequency Data:")
abc = []
for i in elements:
  if not(i in abc):
    abc.append(i)
for i in abc:
  print(f"{i} : {elements.count(i)}")
