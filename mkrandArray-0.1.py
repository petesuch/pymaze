#!/usr/bin/python3.7

################################################################################
#  mkrandArray-0.1.py
#
#  @Author: Peter Suchsland
#  @Date: October 2020
#
#  A creates a two dimensional array (list of lists) and populates it with
#  randomly generated characters based on a weight.
#
################################################################################
#  random.choices is a python3.6 and greater feature
################################################################################

###################################################################################
# EDIT THESE FOR ARRAY SIZE, Window Dimensions, wghtH sets the probability of a
# particular point being the "go" (vs nogo) character.
w = 40          # width
h = 35          # height
spaces = 1      # spaces between characters

wghtH = 0.65       # EDIT THIS NUMBER for probability of go character
wghtL=(1-wghtH)    # low middle point

go='\u2629'     # go character
nogo=' '        # no-go character

"""
Not all unicode characters will print nicely on xterm with utf-8. These do...
'\u271a'    #unicode Open Border Greek Cross bolder
'\u271c'    #unicode Bold Open Center Cross
'\u2719'    #unicode Open Border Greek Cross
'\u271b'    #unicode Open Center Cross
'\u2720'    #unicode Maltese Cross
'\u2629'    #unicode Cross of Jerusalem
"""
###################################################################################
import random
import copy

def printArray(ls, x, y):
    for i in range(y):
        print()
        for j in range(x):
            print(ls[i][j], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(w-1))

myMaze = [ [ random.choices(population=[go,nogo],
    weights=[wghtH, wghtL])[0] for x in range(w)]  for y in range(h) ]

cp = copy.deepcopy(myMaze) # Must use copy.deepcopy
printArray(myMaze, w, h) # Print original array
printArray(cp, w, h) # Print copy of original array
