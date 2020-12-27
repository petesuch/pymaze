#!/usr/bin/python3
#lists on the fly?

"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

import copy
var_one=1
len_one=0
# list of integers
list_one = [[(1,2)],[(3,4)],[(5,6)],[(7,8)],[(7,9),(8,1)]]
print("1.1: list_one:", list_one)
print("1.2: list_one.__len__:", list_one.__len__())

### replace last position
len_one = list_one.__len__()
list_one.append("")     # make it longer by appending nothing
list_one[len_one]=[(2,3)]
print("1.3: list_one: ",list_one)
print("1.4: list_one.__len__():", list_one.__len__())

### make list shorter
temp_one = list_one.pop()
print("1.5: temp_one: ", temp_one)
print("1.6: list_one: ", list_one)
print("1.7: list_one.__len__():", list_one.__len__())

### replace last position
len_one = list_one.__len__()
list_one.append("")     # make it longer by appending nothing
list_one[len_one]=[(33,44)]
print("1.8: list_one: ",list_one)
print("1.9: list_one.__len__():", list_one.__len__())

### add yet another
len_one = list_one.__len__()
list_one.append("")     # make it longer by appending nothing
list_one[len_one]=[(88,99)]
print("2.0: list_one: ",list_one)
print("2.1: list_one.__len__():", list_one.__len__())

### make list shorter again
temp_one = list_one.pop()
print("2.2: temp_one: ", temp_one)
print("2.3: list_one: ", list_one)
print("2.4: list_one.__len__():", list_one.__len__())

### 

### add yet another
len_one = list_one.__len__()
list_one.append("")     # make it longer by appending nothing
list_one[len_one]=[(88,99),(66,22)]
print("2.5: list_one: ",list_one)
print("2.6: list_one.__len__():", list_one.__len__())

### append to last element in list??
len_one = list_one.__len__()
print("2.7: list_one: ",list_one)
print("2.8: list_one[len_one-1]", list_one[len_one-1])
list_temp = copy.copy(list_one[len_one-1])
print("2.9: list_temp: ",list_temp)
len_temp = list_temp.__len__()
list_temp.append("")
list_temp[len_temp]=(47,45)
list_one[len_one-1]=list_temp

"""
print("3.0: list_one:", list_one)
print("3.1: list_one[1]:", list_one[1])
print("3.2: list_one[0].__len__(): ", list_one[0].__len__())
print("3.3: list_one[1].__len__(): ", list_one[1].__len__())
print("3.3: list_one[2].__len__(): ", list_one[2].__len__())
print("3.4: list_one[3].__len__(): ", list_one[3].__len__())
print("3.5: list_one[4].__len__(): ", list_one[4].__len__())
print("3.6: list_one[5].__len__(): ", list_one[5].__len__())
print("3.6: list_one[6].__len__(): ", list_one[6].__len__())


print(list_one[6][0])
print(list_one[6][1])
print(list_one[6][2])

blah=list_one[6][0]
print(blah)
for i in blah:
    if i == 99: 
        print("i equals 99")
    print(i)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
"""
print("4.0: list_one:", list_one)

### print all the elements of each list inside list_one
for x in range(list_one.__len__()):
    print("x: ",x)
    for i in range(list_one[x].__len__()):
        if i > 0:
            print("this list has more than one element")
        print("i: ", i)
        for j in list_one[x][i]:
            print(j)






