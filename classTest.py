#!/usr/bin/python3


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def getPoint(self):
        return (self.x, self.y, self.color)

    def printPoint(self):
        print("x:" , self.x, "y:", self.y)
        print("color: " + self.color)

    def setPointColor(self,color):
        self.color=color


class Maze:
    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize
        self.numofPoints= self.xsize*self.ysize
        

    def getnumofPoints(self):
        return(self.numofPoints)



p1 = Point(12,14, "white")
p1.printPoint()
print(p1.getPoint())
p1.setPointColor("black")
p1.printPoint()
print(p1.getPoint())

p2 = Point(3,4, "black")
p2.printPoint()
print(p2.getPoint())

m1 = Maze(10,10)
print(m1.getnumofPoints())