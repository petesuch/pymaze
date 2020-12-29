#!/usr/bin/python3.7

#   n1.py     An attempt at converting n1.pl to python
#
#   This file is the result of n1.pl parsed through the program perl2python
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
h = 15     # height
spaces = 3    # spaces between characters for screen formatting

wghtH=0.65       # EDIT THIS NUMBER
wghtL=(1-wghtH)    # low middle point

go='x'  # go character
nogo='o'       # no-go character

"""
Not all unicode characters will print on xterm with utf-8. These do...
'\u271a'    #unicode Open Border Greek Cross bolder
'\u271c'    #unicode Bold Open Center Cross
'\u2719'    #unicode Open Border Greek Cross
'\u271b'    #unicode Open Center Cross
'\u2720'    #unicode Maltese Cross
'\u2629'    #unicode Cross of Jerusalem
"""


myMaze = (

[ "A", "o", "o", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "B" ],
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
# These variables need to be changed....

# $tm
# $germ  @branch


i = j = x = y = xs = ys = xp = yp = 0
xprev = yprev = xnew = ynew = xstart = ystart = ""
xleft = yup = ydown = temp = xtemp = ytemp = ""
DONE = False
SOLVED = False

###################################################################################
cp = copy.deepcopy(myMaze) # Must use copy.deepcopy
printArray(myMaze, w, h) # Print original array
printArray(cp, w, h) # Print copy of original array

if cp[0][j] == "x" :
    if ( SOLVED ) break

    print "************************************************************************"
    print "Entering Maze at: (j,0)"
    print "************************************************************************"

    xs = xstart = j
    ys = ystart = 0
    DONE = False

    while not DONE :
        print "********************************************************************"
        print (*** Begin while-loop with: DONE = DONE\n)
        germ = ""
        SOLVED = False
        x = xs
        y = ys
        xprev = xp
        yprev = yp
        cp[yprev][xprev] = "+"
            xright = x+1
            xleft = x-1
            yup = y+1
            ydown = y-1
            counter = 0
            # show xprev and yprev
            # print (xprev = xprev\n\$yprev = yprev)
            # print ("\n### In while-loop with:(x,y) ###a")

            # check below
            if cp[ydown][x] == "x" :
                # addbud($x,$y,$x,$ydown)
                counter += 1
            # check to the right
            if cp[y][xright] == "x" :
                # addbud($x,$y,$xright,$y)
                counter += 1
            # check to the left
            if cp[y][xleft] == "x" :
                # addbud($x,$y,$xleft,$y)
                counter += 1
            # check above
            if cp[yup][x] == "x" :
                # addbud($x,$y,$x,$yup)
                counter += 1

        #########    # there yet?
        if cp[yup][x] == "x" & yup == "19" :
            SOLVED = "YES"
            print "************* FINISH ***************"
            DONE = "YES"
                #print "# there yet? \$DONE is $DONE\n"
            cp[$y][$x] = "+"
            cp[$yup][$x] = "+"


        print "Branch Array \@branch contains these points:\n(@branch)"
        #print "Branch Array Created B$xstart with these points:\n($B[$xstart])\n"

        #########    # not dead
        if counter gt 0 :
            # addbranch($germ)
            print "Array", germ contains the following points:\n(@$germ)
            # temp = pop @$germ
            # ($xnew, $ynew) = split(/\,/, $temp)

            print xnew,ynew
            print "The value of", germ:(@$germ)

            xp = x
            yp = y

            xs = xnew
            ys = ynew

            ##### dead end

        if counter == 0 :
            print "\nDEAD END:", x,$y
            tm = pop @branch
            print "\t \@tm = (@tm)"
            # until ( "@$tm" != "" | "$#branch" == "-1" ) {

            tm = pop @branch
            #print "\@$tm = @$tm\n"
            #print "DURING:\t$tm contains: (@$tm)\n"
            #print "DURING: the branch has: @branch\n"
            # if last element not empty push back on the branch
            if "@tm" != "" :
                print "BEFORE: @branch"
                print "pushing back on the branch:"
                print "because", tm contains: (@$tm)
                # push @branch, $tm

            print "AFTER: @branch"
            #### pop the bud
        temp = pop @tm
        # ($xtemp, $ytemp) = split( /,/, $temp)


        if xtemp != "" & ytemp != "" :
            xs = xtemp ys = ytemp

        elif xtemp == "" & ytemp == "" :
            print "xtemp and ytemp are NULL"
            print "###  branch: @branch"
            DONE = "YES"
        print "PITSTOP: xs:(xs),ys:(ys)"

    print \n#### END of while-loop:\$DONE is DONE
    print "\n\xs:(xs),\ys:(ys),\xp:(xp),\yp:(yp)"
    print "#  branch: @branch"
    print "#### END of while-loop:\$DONE is DONE"_
    print "#######################################################"
    cp[$y][$x] = "+"

    # printarray() sleep 2
    }
}

if SOLVED :
    print ("***************************************************")
    print ("**********  Maze Solved  **************************")
    print ("***************************************************")

elif not SOLVED :
    print ("***************************************************")
    print ("*****   Maze Not Solved  **************************")
    print ("***************************************************")

# printArray(ar,x,y)

#### END main program #########################################################
### SUBROUTINES ###############################################################

def addbud():
    germ = "G_[0]_[1]"
    if @germ:
        # push @$germ, "$_[2],$_[3]"
    else:
        # @$germ= ( "$_[2],$_[3]" )

def addbranch():
    #$branch = "B[$xstart]" # ie B3
    if @branch :
        # push @branch, "$_[0]"
    else:
        # @branch = ( "$_[0]" )
        # print "Branch Array Created $branch with these points:\n(@$branch)\n"

# takes a list of lists and dimensions
def printArray(ls, x, y):
    for i in range(y):
        print("\n")
        for j in range(x):
            print(ls[i][j], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(w-1))
