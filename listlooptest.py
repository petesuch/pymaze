#!/usr/bin/python3

lol= [11, [22],[33,44,55], [1, 'a string', ['the Wright Brothers', 77, 28, 'zzzz'], 678], 'yesterday', 'b string']




    
def fun1(lst):
    print("fun1 was called")
    for i in lst.__iter__():
        #print(i)
        if (isinstance(i, int)):
            print("found an integer: ", i)
        elif (isinstance(i, str)):
            print("found a string: ", i)
        elif (isinstance(i, list)):
            print("found a list: ", i)
            fun1(i) # recursively called again if nested list is found




fun1(lol)
print(lol)
