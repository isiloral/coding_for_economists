#In this file, we'll look at lists, dictionaries, set, tuples, range

#List #square brackets implies lists
myList = [1, 2, 3, 4, 5]
print(myList)
print(type(myList)) # <class 'list'>

#grab first object of the list
print(myList[0]) #1

#How many object are in our list?
print(f'Our list object myList has {len(myList)} elements')

#Nice thing about lists: they are flexible with respect to the data type
mixedList = [1, 'two', 3.0, [4, 'four'], 5]
print(mixedList)

#We can also add and remove objects from a list
mixedList.append(6)
print(mixedList)

#Removing
mixedList.pop() #without an argument, it removes the last item
print(mixedList)

#How many times does the integer 1 appear?
print(mixedList.count(1))

#Reverse a list
mixedList.reverse()
print(mixedList)

