#!/usr/bin/python3
#array on the fly?

"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

"""

var=1
len=0
# list of integers
my_list = [[(1,2)],[(3,4)],[(5,6)],[(7,8)],[(7,9),(8,1)]]
print("1.1. my_list.count:",my_list.__len__())
len=my_list.__len__()
print("1.2 ", my_list)


# replace last position
my_list.append("") # make it longer by appending nothing
my_list[len]=[(2,3)]

print("1.3. ",my_list)
print("1.4. my_list.count:", my_list.__len__())

temp_1= my_list.pop()  # now make it shorter
print("1.5. temp: ",temp_1)
print("1.6. ", temp_1[0])
#print("1.7. ", temp_1[1])
print("1.8. ", my_list)
print("my_list.count:",my_list.__len__())

# longer again with different values
my_list.append("") # make it longer by appending nothing
my_list[len]=(9,9)
print("My list after adding another set: ",my_list)

len=my_list.__len__()
for i in range(len):
    print("1. my_list at: " ,i, my_list[i])

temp_2=my_list[4]
print("1. temp2 now is: ", temp_2)
print("temp2 length:", temp_2.__len__())

for i in temp_2:
    print("temp2:", i)

temp_2.append("") # make it longer by appending nothing

len=temp_2.__len__()
temp_2[len]=(99,33)

print("2. temp2 now is: ", temp_2)

my_list[4]=temp_2


len=my_list.__len__()
for i in range(len):
    print("3. my_list at: " ,i, my_list[i])

"""


print(my_list[var])
print(my_list[var][var])



## append at position 2?
my_tup=my_list[var]
print(my_tup)

my_tup=my_tup+(22,3,) # comma needed
print(my_tup)

my_tup=my_tup+(var+1,22,) # comma needed
print(my_tup)

my_list[var]=my_tup
print(my_list)

my_list.pop()
print(my_list)

my_list.pop()
print(my_list)
print("my_list.count:",my_list.__len__())

my_list.pop()
print(my_list)
print("my_list.count:",my_list.__len__())



## append to my_list at the end
my_list.append("99,11")
print(my_list)

# empty list
my_list = []
print(my_list)

# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)
print(my_list[var+1])
print(var)
print(my_list.__getattribute__)
my_list= "helo"

dct = {'x': 1, 'y': 2, 'z': 3}
print(dct)
print(dct["y"])
"""