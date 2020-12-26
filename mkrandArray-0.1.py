#!/usr/bin/python3.7

#  mkrandArray-0.1.py
#  @Author: Peter Suchsland
#  @Date: October 2020
#
#  A one liner version of creating a two dimensional array (list of lists) and
#  populating it with randomly generated characters based on a weight.

import random
import copy

w=33     # width
h=15     # height
spaces=3    # spaces between characters

wghtH=0.65       # EDIT THIS NUMBER
wghtL=(1-wghtH)    # low middle point

go='\u2629'  # go character
nogo=' '       # no-go character

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
    print("\n~"+"~"*(spaces+1)*(w-1))

###################################################################################
#  I am not sure random.choices is worth the effort !!!
#  Sure its great to create a random 2 dimensional array filled with random
#  characters all in one line but it's only a python3.6 feature and it is confusing.
#  On the other hand a dynamic array class is not needed.
###################################################################################

myMaze4 = [ [ random.choices(population=[go,nogo],weights=[wghtH, wghtL])[0] for x in range(w)]  for y in range(h) ]

#cpy = copy.deepcopy(myMaze1)   # Must use copy.deepcopy

printArray(myMaze4, w, h) # Print original array