# pyMazeSolver.py

"""
    aka: n2.py

    A Python version of a perlMazeSolver.pl
    A Maze Solving Program
    Working on: 01/21/2021

    @author:  Peter A. Suchsland
    @Date: Jan 2021

    TODO:
    There are still a few bugs with the logic concerning the edges of the array.
    Later versions will have user supported Mazes as seperate files

    A strict tuple structure maintained throughout the program:
    ('G9_12', ((9,11), (8,12), (10,12)))
    ('G9_12', ((9,11), (8,12), ))
    ('G9_12', ((9,11),))
"""
# START
import sys, copy, collections

# EDIT These to match array to terminal window
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

#####################################################################################################################################################################

# A copy is used for manipulation
cp = copy.deepcopy(maze)    # Must use copy.deepcopy

DONE,SOLVED = False,False
x = ""; y = ""; xp = ""; yp = ""
germdict = collections.OrderedDict() # dictionary
germ = ''; i=j=0

# prints out a List of Lists
def printArray(ls, _x, _y):
    _i=_j=0
    for _j in range(_y):
        print()
        for _i in range(_x):
            print(ls[_j][_i], end=' '*spaces)
    print("\n~"+"~"*(spaces+1)*(w-1))

# Show Variables While looping
def printVariables():
    print()
    print("i:",i, " j:",j, " x:",x, " y:",y, " xp:",xp, " yp:",yp)
    print("DONE:",DONE," SOLVED:",SOLVED)
    print("germdict: ", germdict)

# Tuple Expanding -- sometimes tuples can get overly nested.
# Removes multiple levels of nesting
def te(t):
    lst=[]
    newlst =[]
    def re(t): # Recursive expansion
        for element in t:
            if isinstance(element, tuple) :
                re(element)
            if isinstance(element, int) :
                lst.append(element)
    re(t)
    # for grouping
    len = (lst.__len__())/2
    len = int(len)
    #print("After Tuple Expansion: ")
    for i in range(len):
        newlst.append( (lst[2*i],lst[2*i+1]) )
    return(tuple(newlst))

#
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
#
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
#
for j in range(w):
    if (cp[0][j] == go ):
        if ( SOLVED ):
            break
        print ("**************************************************************")
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
            try:    # yup is the last go
                 if ( ( cp[yup][xup] >= go) and (yup >= SZ-1 ) ) :
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
            print ("# Loop End ###############################################")

if SOLVED:
    print ("*****  MAZE SOLVED  *******************************")
if not SOLVED:
    print ("*****  MAZE NOT SOLVED  ***************************")

printArray(cp,w,h)
printVariables()

# END

