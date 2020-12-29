#!/usr/bin/python3.7
#
#   Point.py
#
#   a simple class to help with the maze solver.
#   here is some testing demonstrating functionality needed.  For example,
#   a list can contain Point objects, which can be appended or popped like a stack.

#   In my previous Perl version of the mazesolver, I created arrays with new names
#   based on a point: ie G23 or G1312. I have been worried that I will need that
#   same functionality in Python, but am slowly coming to believe that it is not
#   necessary nor never was necessary. At this point, my understanding is that if I
#   can stack points on one list and access them after multiple pops I will not
#   need multiple lists.  This is of-course for maze solving.
#
#   I have decided to name the copied maze the "working model" or "active model"
#   The point where decisions are made will be called the "head"

#   I find it strange that Python object can have properties that can be changed:
#   with or without getters and setters, meaning that the insides of a Python Ojbect
#   are never completely hidden.  Am I wrong?

#   Is it possible to create a Typed List?  .... that accepts only Point objects
#   for example????

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPoint(self):
        return (self.x, self.y)

    def getX(self):
        return (self.x)

    def getY(self):
        return (self.y)

    def printPoint(self):
        print("x:",self.x,"y:",self.y)


class Branch:
    def __init__( self, Point ):
        self.branch = list(range(10))
        self.branch.append(Point)

    def addBud(self, Point ):
        self.branch.append(Point)

    def popBud( self ):
        return( self.branch.pop() )

    def getLen(self):
        return (self.branch.__len__())

    def printBranch(self):
        for obj in self.branch:
            if type(obj) == Point:
                print ( obj.getPoint() )



p1 = Point(11,11)
p2 = Point(22,22)
p3 = Point(33,33)
p4 = Point(44,44)


b1 = Branch(p1)

b1.printBranch()

b1.addBud(p2)

print ("*****")
b1.printBranch()
print ("*****")

print ("***", b1.getLen(),"*****")


w=2
h=5
SZ =w*h

#branch = [None] *  SZ

"""

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
