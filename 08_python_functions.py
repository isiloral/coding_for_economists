#about functions

#function definition syntanx
def add_one(num): #just like loops, name anything (num=banana)
  return num + 1 #typically you find a return statement

print(add_one(5)) #prints 6

#function without return statement and without arguments
def add_one_str():
  print(6)

print(add_one_str())

#try to assign the output of a function to a variable
res = add_one(5)
res_str = add_one_str()

print(res, res_str)

#multiple return values
def add_one_return_both(num1):
  return num1, num1 + 1

print(add_one_return_both(5))
print(type(add_one_return_both(5)))

#more than 1 argument in functions
def add_two_nums(num1, num2):
  res = num1 + num2
  return num1, num2, res

print(add_two_nums(6, 7))

#default values for function arguments
def exponentiate(num, exponent=2):
  return num**exponent

print(exponentiate(5, 2) == exponentiate(5))

#keyword arguments: using the argument name to assign a value; here, order does not matter
print(exponentiate(exponent=3, num=5))

#functions with variable number of argumnets
def add_nums(*nums):
  res = 0

  for num in nums:
    res += num
  return res

print(add_nums(1, 2, 3, 4, 5))

#lets try to code up some docstrings for a function 
def cast_listitems_to_str(list_of_objects):
  """
  Casts all items in a list to a list of string
  
  Parameters:
  ------------------------
  list_of_objects: list

  Returns: 
  ------------------------
  list_of_strings: list
  """
  list_of_strings = []
  for element in list_of_objects:
    list_of_strings.append(str(element))

  return list_of_strings

#print(list_of_strings) #outside of local scope
#print(cast_listitems_to_str([1, '2', 2, 5]))

#print(help(cast_listitems_to_str))

#scope of a variable 
def test(a,b):
  c = a + b #scope of 'c' is confined to function
            #'c' is said to have lcoal scope
c = 5 #Here, 'c' has a global scope

#lambda functions (aka anonymous functions)
#reference function
def square(x):
  """
  Returns the square of x
  
  Parameters:
  ------------------------
  x: int or float or double
  
  Returns:
  ------------------------
  square_x: int or float or double
  """
  return x**2

#equivalent lambda function
square_lambda = lambda x: x**2

#compare the output
print(square(5) == square_lambda(5))
  
  