#!/usr/bin/python3.7
#  mkrandarray.py
#
#  uses the concept of a dynamic list to create a random array of crosses.
#
#  @author Peter Suchsland
#  @date December 2020

import random
import copy

varx=33 #width
vary=15 #height

spaces=3 #spaces between characters

ranh=1100 # random high
ranl=500 #low middle point

g='\u2629'  # go character
n=' '       #no go character

"""
Not all unicode characters will print on xterm with utf-8. These do...
'\u271a'    #unicode Open Border Greek Cross bolder
'\u271c'    #unicode Bold Open Center Cross
'\u2719'    #unicode Open Border Greek Cross
'\u271b'    #unicode Open Center Cross
'\u2720'    #unicode Maltese Cross
'\u2629'    #unicode Cross of Jerusalem
"""

def printArray(ls, x, y):
    for i in range(y):
        print("\n")
        for j in range(x):
            print(ls[i][j], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(varx-1))


class dynamiclist(list):
    """ List not needing pre-initialization
    Example:
        l = dynamiclist()
        l[20][1] = 10
        l[21][1] = 20
    """
    def __setitem__(self, index, value):
        size = len(self)
        if index >= size:
            self.extend(dynamiclist() for _ in range(size, index + 1))
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        size = len(self)
        if index >= size:
            self.extend(dynamiclist() for _ in range(size, index + 1))  # allows dimensions > 1
        return list.__getitem__(self, index)


dl = dynamiclist()

for i in range(vary):
    for j in range(varx):
        if random.randrange(ranh) > ranl:
            dl[i][j]=g  #go character
        else:
            dl[i][j]=n  #no-go character

cpy = copy.deepcopy(dl)     # Must use copy.deepcopy
printArray(cpy, varx, vary) # Print original array
