#let's have a look at loop syntax

#for loop operate on "iterables (everything that you can index)"

#Lets create an iterable object
myList = [1, 2, 'abc']

#Lets iterate over the object
for banana in myList:
  #loop body needs to be indented once
  if banana == 1:
    print(banana)
  else:
    print('item not equal to 1')

# Looping over a range of values
print("Using range(5)")
for i in range(5): #range() generate value on the fly
  print(i)

#Another way to do it
range_vals = [0, 1, 2, 3, 4] #not memory efficient
print('using a list to display values 0-4')
for i in range_vals:
  print(i)

#Looping over list of strings and nesting loops
for name in ['James', 'Jane', 'Jack']:
  print(name)
  # Iterate through each string
  for letter in name:
    print(letter)

# Using the enumerate() function to get both index and value
print("Using enumerate()")

for index, name in enumerate(['James', 'Jane', 'Jack']):
  print(index, name)

#Equivalent loop using indexing
print('Using range() and indexing')
myList = ['Alice', 'Bob', 'Charlie ']
for index in range(len(myList)): #range(3)
  print(index, myList[index])

#Use a loop to create a list of capital letters from A-Z
print('Using a loop to create a list of capital letters from A-Z')
#Instantiate an empty list to append to 
alphabet = []
for i in range(65, 91):
  print(i, chr(i))
  alphabet.append(chr(i))

print(alphabet)

#while loops 
#while loops are used when you don't know how many times you want to loop

#Instantiate counter variable
i = 0
while i < 10:
  #do sth
  print(i)
  #Increment our counter every iteration otherwise it will loop forever 
  i += 1

#List comprehensions
#List comprehensions are a way to create a list in one line of code
#Let's have a look at a for loop creating a list of squares from 0 to 10
squares = []
for num in range(0, 11):
  squares.append(num**2)

print(squares)

#Do the same thing using list comprehension in 1 line
squares = [num**2 for num in range(0, 11)] #computationally faster tha for loops
print(squares)

#List comprehension with conditionals (using if in list comprehension)
even_squares = [num**2 for num in range(0, 11) if num % 2 == 0]

print(even_squares)


