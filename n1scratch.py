#!/usr/bin/python3.7

#   n1scratch.py
#
#       a testing file for python code
#
#   @author: Peter Suchsland

###############################################################################
# TODO:
# Learn how to creates variables and arrays in python
# Learn proper syntax for while, if loops
# Proper indentation
###############################################################################

#### START main program
import sys
import random
import copy

#EDIT THIS to match array
w = 20     # width
h = 20     # height
spaces = 3    # spaces between characters for screen formatting

myMaze = (
[ "x", "o", "o", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "B" ],
[ "o", "x", "x", "x", "x", "x", "x", "x", "x", "o", "o", "o", "o", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "o", "x", "x", "o", "x", "o", "x", "o", "o", "o", "x", "x", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "o", "o", "x", "o", "x", "o", "x", "x", "o", "o", "x", "o", "o", "o", "o", "o", "x", "o" ],
[ "o", "x", "o", "o", "x", "o", "x", "x", "o", "x", "o", "o", "x", "x", "x", "x", "x", "o", "x", "o" ],
[ "o", "x", "o", "o", "x", "o", "x", "o", "x", "x", "x", "o", "o", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "o", "x", "o", "x", "x", "x", "x", "o", "x", "o", "o", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "x", "o", "x", "o", "x", "o", "x", "o", "x", "x", "x", "x", "o", "o", "x", "x", "x", "o" ],
[ "o", "o", "x", "o", "o", "o", "o", "o", "x", "o", "o", "o", "o", "o", "x", "x", "x", "o", "x", "o" ],
[ "o", "o", "x", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "x", "o", "x", "o" ],
[ "o", "x", "o", "o", "x", "x", "x", "x", "x", "o", "x", "x", "x", "o", "x", "x", "x", "o", "x", "o" ],
[ "o", "x", "x", "x", "o", "x", "x", "x", "x", "o", "x", "o", "o", "o", "x", "o", "x", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "o", "x", "x", "x", "o", "x", "o", "x", "o", "x", "o", "x", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "x", "o", "x", "x", "o", "x", "x", "x", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "x", "x", "x", "x", "o", "x", "o", "x", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "x", "x", "o", "x", "o", "x", "o", "x", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "x", "x", "o", "x", "x", "x", "o", "x", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "x", "x", "x", "x", "o", "o", "o", "x", "o", "x", "o", "o", "o", "x", "o" ],
[ "o", "x", "x", "x", "x", "x", "x", "x", "x", "o", "o", "o", "x", "o", "x", "x", "x", "x", "x", "o" ],
[ "C", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "x", "o", "o", "o", "Z" ]
)

###################################################################################
i = j = x = y = xs = ys = xp = yp = 0
xprev = yprev = xnew = ynew = xstart = ystart = ""
xleft = yup = ydown = temp = xtemp = ytemp = ""
DONE = False
SOLVED = False
###################################################################################
def printArray(ls, x, y):
    for i in range(y):
        print()
        for j in range(x):
            print(ls[i][j], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(w-1))
###################################################################################
def printVariables():
    print()
    print("i: ",i, "j: ",j, "x: ",x, "y: ",y, "xs: ",xs, "ys: ",ys, "xp: ",xp, "yp: ",yp)
    print("xprev: ",xprev, "yprev: ",yprev, "xnew: ",xnew, "ynew: ",ynew, "xstart: ",xstart, "ystart: ",ystart)
    print("xleft: ",xleft, "yup: ",yup, "xnew: ",xnew, "ynew: ",ynew, "xtemp: ", xtemp, "ytemp: ", ytemp)
    print("DONE: ",DONE,"SOLVED: ",SOLVED)
###################################################################################

cp = copy.deepcopy(myMaze) # Must use copy.deepcopy
printArray(myMaze, w, h) # Print original array
printArray(cp, w, h) # Print copy of original array

for i in range(w) :
    if (cp[0][j] == "x"):
        if ( SOLVED ):
            break
        print ("************************************************************************")
        print ("Entering Maze at: (j,0)")
        print ("************************************************************************")
        xs = xstart = j
        ys = ystart = 0
        DONE = False
        printVariables()
