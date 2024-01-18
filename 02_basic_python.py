#basic arithmetic operations in python

#add 2 numbers
print(2+4)

#Divide 2 numbers
print(10/5)
#careful: division returns a float
print(type(10/5))

# exponentiation
print(2**3)

# Assigning variables
x = 5
y = x ** 2
print(y)

# String
a = "Hello how're you?" #equivalently 'Hello'
#If you have apostrope in your string, then use double quotes

#arithmetic operations on strings
#multiplication
print(a*5)

#Concatenation
b = "I'm good, thank you"
print(a + " "+ b)

#substraction
# print(a - b)

#division
#print(a / b)

#Indexing and slicing
#First element
print(a[0])

#Last element
print(a[-1])

#Slicing
print(a[0:5])

#How many characters does our string have? 
#print(len(a))
#whatever you wanna evaluate, put into curly braces in the form below: 
print(f'Our string a has {len(a)} characters')

#Alternatively
print('Our string a has {} characters'.format(len(a)))

#have a look at logical statements
print(2 == 2) #True #equivalent to 1

print(2 == 3) #False #equiavlent to 0

#Check if True and 1 are in fact equivalent
print(True == 1)

#True evaluates to 1 an False evaluates to zero
print(True + True + True)

#Check equivalence of two variables
print (a == b)

#Multiple logical statements
print(2 == 2 and 3 == 3) #True
print(2 == 2 and 3 == 4) #False

print(2 == 2 or 3 == 4) #True
print(2 == 3 or 3 == 4) #False
