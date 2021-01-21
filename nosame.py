#!/usr/bin/python



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



a1 = Point(1,1)
a2 = Point(1,1)
a3 = Point(1,1)
a4 = Point(1,1)
a5 = Point(1,1)

b = Point(1,1)
c = Point(3,3)
c = Point(3,3)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(b)
print(c)
print(c.getY())

