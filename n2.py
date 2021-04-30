#!/usr/bin/python3.8

#   PYTHON VERSION of mazeSolver
#   A maze solving program
#
#   n2.py
#
#   @author:  Peter A. Suchsland
#   @Date: Jan 2021

###################################################################################
# TODO:
#
#   *   Working on: 01/21/2021
#   *   A strict tuple structure should be maintained throughout the program:
#   *   ('G9_12', ((9,11), (8,12), (10,12)))
#   *   ('G9_12', ((9,11), (8,12), ))
#   *   ('G9_12', ((9,11),))
#
###################################################################################
#### START main program
import sys
import random
import copy
import collections

#EDIT THIS to match array
w = 40          # width
h = 40          # height
spaces = 1      # spaces between characters for printing to screen
SZ = 40         # size of array == h

go = 'x'
nogo = 'o'
mark = '+'

#####################################################################################################################################################################
maze = (
["A","o","o","x","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","B"],
["o","o","o","x","o","o","o","o","o","x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","x","x","o","x","x","x","x","x","x","x","x","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","x","x","x","x","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","x","x","o","o","o","o","o","o"],
["o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o"],
["o","o","o","o","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o"],
["x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","x","x","o","o","o","o","o","o"],
["x","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","x","x","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","x","x","x","o","o","x","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","x","x","o","x","x","x","x","x","x","x","o","x","x","x","x","x","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","x","x","x","x","o","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","o","o","x","o","x","o","x","x","x","x","o","o","o","o","x","o","o","x","o","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","x","x","x","o","x","o","x","o","o","x","o","o","o","o","x","o","o","x","x","o","o","o","x","o","o","x","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","x","o","x","o","o","x","o","o","o","o","x","o","o","o","x","o","o","o","x","o","o","x","x","x","x","x","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","x","x","x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","x","o","o","o","o","o","o","x","x","x","x","x","x","x","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","x","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","x","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","o","o","o","o","o","x","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","o","o","o","o","o","o","o","o","o","x","x","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["x","x","o","o","o","o","o","o","o","o","o","o","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o"],
["C","x","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","o","Z"]
)

###################################################################################
# used for manipulations
cp = copy.deepcopy(maze)    # Must use copy.deepcopy

###################################################################################
DONE = False; SOLVED = False
x = ""; y = ""; xp = ""; yp = ""
germdict = collections.OrderedDict() # dictionary
germ = ''; i=j=0
###################################################################################
def printArray(ls, _x, _y):
    _i=_j=0
    for _j in range(_y):
        print()
        for _i in range(_x):
            print(ls[_j][_i], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(w-1))
###################################################################################
def printVariables():
    print()
    print("i:",i, " j:",j, " x:",x, " y:",y, " xp:",xp, " yp:",yp)
    print("DONE:",DONE," SOLVED:",SOLVED)
    print("germdict: ", germdict)
###################################################################################

###################################################################################
### tuple expand -- sometimes tuples can get overly nested this removes
###  multiple levels of nesting
def te(t):
    lst=[]
    newlst =[]
    def re(t): ### recursive expand
        for element in t:
            if isinstance(element, tuple) :
                re(element)
            if isinstance(element, int) :
                lst.append(element)

    re(t)
    ### for grouping
    len = (lst.__len__())/2
    len = int(len)
    #print("After Tuple Expansion: ")
    for i in range(len):
        newlst.append( (lst[2*i],lst[2*i+1]) )

    return(tuple(newlst))
###################################################################################
def addbud(x,y,a,b):
    germ = "G"+str(x)+"_"+str(y)
    if (germdict.__contains__(germ)):
        val = germdict[germ]
        germdict[germ] = te((val,(a,b)))
        print("germdict", germdict)
    else:
        exec("%s = []" % germ)
        germdict[germ] = te((a,b))
        print("germdict", germdict)
###################################################################################
def popGetXY():
    if (germdict.__len__() > 0):
        val = germdict.popitem(last=True)
        if ( (val.__len__() > 1) and (val[1].__len__() > 0 )) :
            print("val[0]: ",val[0])
            print("val[1]: ",val[1])
            lsv = list(val[1])
            (x,y) = lsv.pop()
            if lsv.__len__() > 0:
                germdict[val[0]] = tuple(lsv)
            print("popGetXY: germdict: ", germdict)
            return (x,y)
        else:
            return False
    else:
        return False
###################################################################################
for j in range(w):
    if (cp[0][j] == go ):
        if ( SOLVED ):
            break
        print ("************************************************************************")
        print ("Entering Maze at: 0,", i )
        DONE = False; xentry = j; yentry = 0; x = xentry; y = yentry;

        while not DONE:
            print ("starting while loop")
            printVariables()
            printArray(cp,w,h)

            SOLVED =  False; xp = x; yp = y; germ = ""; cp[y][x] = mark

            #print ("marking cp: ", yp,",", xp)

            xright = x+1; yright = y; xleft = x-1; yleft = y
            xup = x; yup = y+1; xdown = x; ydown = y-1; counter = 0

            ### Check Down
            try:
                if ( cp[ydown][xdown] == go ) :
                    addbud(x,y,xdown,ydown)
                    counter+=1
            except:
                pass
            ### Check Right
            try:
                if ( cp[yright][xright] == go ) :
                    addbud(x,y,xright,yright)
                    counter+=1
            except:
                pass
            ### Check Left
            try:
                if ( cp[yleft][xleft] == go ) :
                    addbud(x,y,xleft,yleft)
                    counter+=1
            except:
                pass
            ### Check Above
            try:
                if ( cp[yup][xup] == go ) :
                    addbud(x,y,xup,yup)
                    counter+=1
            except:
                pass

            ### There Yet?
            try:
                if ( ( cp[yup][xup] >= go) and (yup >= SZ-1 ) ) :  # if yup is a go and the last
                    SOLVED = True; DONE = True
                    cp[yup][xup] = mark # if its there mark it
                    break
            except:
                pass
            ### Not Dead
            if ( counter > 0 ) :
                print("counter greater than 0")
                try:
                    chx, chy = popGetXY()
                    print("x:",x)
                    print("y:",y)
                    #print(germdict)

                    x = chx; y = chy
                    #print("x: ",x , " y: ", y)
                except:
                    pass

            ### Dead End
            if ( counter == 0 ) :
                print("counter equal to 0")
                try:
                    chx, chy = popGetXY()
                    x = chx; y = chy
                    #print("x: ",x , " y: ", y)
                except:
                    if j == w-1:
                        DONE =True
                    break

            printVariables()
            printArray(cp,w,h)
            print ("# Sleeping ###################################################")

if SOLVED:
    print ("*****  MAZE SOLVED  *******************************")
if not SOLVED:
    print ("*****  MAZE NOT SOLVED  ***************************")
printArray(cp,w,h)
printVariables()

#### END main program

