#!/usr/bin/python

#   Point.py

#   a simple class to help with the maze solver.
#   here is some testing demonstrating functionality needed.  For example,
#   a list can contain Point objects, which can be appended or popped like a stack.

#   In my previous Perl version of the mazesolver, I created arrays with new names
#   based on a point: ie G23 or G1312. I have been worried that I will need that
#   same functionality in Python, but am slowly coming to believe that it is not
#   necessary nor never was necessary. At this point, my understanding is that if I
#   can stack points on one list and access them after multiple pops I will not
#   need multiple lists.  This is of-course for maze solving.  Btw, that really is
#   a pretty cool feature of Perl.

#   I have decided to name the copied maze the "working model" or "active model"
#   The point where decisions are made will be called the "head" or "head point"

#   I find it strange that Python objects can have properties that can be changed:
#   with or without getters and setters, meaning that the insides of a Python Ojbect
#   are never completely hidden.  Am I wrong?

#   Is it possible to create a Typed List?  .... that accepts only Point objects
#   for example? with a LIFO add/remove strategy?


#   I would like to create a Point class that does not accept identical coordinates
#   For example, "object status" is not given to the second of two points with the
#   same coordinates of (3,14).

#   And/Or a Branch class that does not accept identical point coordinates. This might
#   be the better/easier solution.

class Point:

    _point_objects = {}

    def __new__(self, x, y):
        print("starting new...")
        _name = "P:"+str(x)+"_"+str(y)

        print ("name: ", _name)

        try:
            print("cls: ", self._point_objects[_name])
            return self._point_objects[_name]

        except KeyError:
            pass

        obj = super().__new__(self)
        self._point_objects[_name] = obj
        print ("obj: ", obj)
        return obj

    def __init__(self, x,y):
        print("starting init...")
        self._x = x
        self._y = y
        self._name = "P:"+str(x)+"_"+str(y)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getName(self):
        return self._name

    def getPoint(self):
        return (self._x, self._y)




class BrokenPoint:
    # Is it possible to create a class that will not create duplicates?

    # create dict of name : object pairs
    _point_objects={}

    def new(cls, x, y):
        self._name = 'P:'+str(x)+'_'+str(y)
        if (cls._point_objects.__contains__(self._name) ):
           return cls._point_objects.__getitem__(cls._name)
        else:
            cls._point_objects.__setitem__(cls._name, cls)
            return self

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._name = 'P:'+str(x)+'_'+str(y)

    def printPoint(self):
        print("x:",self._x,"y:",self._y)


class Branch:

    def __init__( self, p ):
        self.branch = list(range(20))
        self.mySet = set()
        self.mySet.add((p.getX, p.getY))
        self.branch.append((p.getX,p.getY))

    def pushBud(self, p ):
        if type(p) == Point:
            previousLength=self.mySet.__len__()
            self.mySet.add((p.getX,p.getY))
            newLength=self.mySet.__len__()
            if ( newLength > previousLength):
                self.branch.append((p.getX,p.getY))

    def popBud( self ):
        popped=self.branch.pop()
        self.mySet.discard(popped)
        return(popped)

    def getLen(self):
        return (self.branch.__len__())

    def printBranch(self):
        for item in self.branch:
            print ( item )


p1 = Point( 1, 1 )

print(p1.getName())
"""
p2 = new Point(2,2)
p3 = new Point(3,3)
p4 = new Point(4,4)
p5 = new Point(5,5)
p6 = new Point(6,6)
p7 = new Point(4,4)
p8 = new Point(4,4)
p9 = new Point(4,4)


if (p9==p4) :
    print ("they are equal")
else :
    print ("different objects")

b = Branch(p1)

#print("b.printBranch(): " , b.printBranch())

b.pushBud(p2)
b.pushBud(p2)
b.pushBud(p2)
b.pushBud(p2)
b.pushBud(p2)
b.pushBud(p3)
b.pushBud(p4)
b.pushBud(p5)
b.pushBud(p6)
b.pushBud(p7)
b.pushBud(p8)
b.pushBud(p8)
b.pushBud(p8)
b.pushBud(p8)
b.pushBud(p8)
b.pushBud(p8)
b.pushBud(p9)

#print ("*****")
#print("b.printBranch(): " , b.printBranch())

#print ("***", b.getLen(),"*****")
###################################################################################

w=2
h=5
SZ =w*h

#b.popBud().printPoint()
#g=b.popBud()
#print("type of g: ", type(g) )
#if ( type(g) == Point ) :
#    print ("g is a point " )

#b.addBud(3) # these should do nothing because not a Point
#b.addBud(3333)
#b.addBud("happy")

print("b.printBranch(): " , b.printBranch())
print ("*****")

import queue

q1 = queue.LifoQueue()

q1.put(p1)
q1.put(p2)
q1.put(p3)
q1.put(p4)
q1.put(p4) # why is this getting added? Not what I want.
q1.put(p4)

print( "q1.get(): ", q1.get().printPoint() )
print( "q1.get(): ", q1.get().printPoint() )
print( "q1.get(): ", q1.get().printPoint() )
print( "q1.get(): ", q1.get().printPoint() )


#branch = [None] *  SZ
branch = list(range(SZ))

for i in range(SZ):
    branch[i]=Point(1,1)
print ("*****")


for obj in branch:
    if type(obj) == Point:
        print ("yes its a point")
        print ( obj.getPoint() )
    else :
        #print("no its not a point")

branch[4]=Point(3,3)
branch.append(p1)

print("printing list:")
for obj in branch:
    if type(obj) == Point:
        print ("yes its a point:", obj.getPoint() )
    else :
        print("not a point:",obj)

print ("#####")
p=branch.pop()
p.printPoint()
newX = p.getX() +100
print("newX:",newX)

p=branch.pop()
p.printPoint()
p=branch.pop()
p.printPoint()
newX = p.getX() +100
print("newX:",newX)

print("lenght of list: ", branch.__len__())

branch.append(p2)
branch.append(p3)
branch.append(p4)

print("lenght of list: ", branch.__len__())

print("printing list:")
for obj in branch:
    if type(obj) == Point:
        print ("yes its a point:", obj.getPoint() )
    else :
        print("not a point:",obj)

"""
