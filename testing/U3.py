#!/usr/bin/python3.8

#
#   A Class that does not allow multiple instances to have identical values.
#   Attempts to create new objects with the same values are returned the first
#   original instance.
#

class Point:
    instances = {}

    def __new__(cls, val1, val2):
        try:
            return cls.instances[val1,val2]
        except KeyError:
            pass

        obj = super ().__new__(cls)
        cls.instances[val1,val2] = obj
        return obj
    def __init__(self, val1,val2):
        self.val1 = val1
        self.val2 = val2
    def getX(self):
        return self.val1
    def getY(self):
        return self.val2
    def getPoint(self):
        return (self.val1, self.val2)


a1 = Point(1,1)
a2 = Point(2,2)
a3 = Point(1,1)
a4 = Point(1,1)
a5 = Point(5,5)
a5 = Point(5,5)
a6 = Point(5,5)
a7 = Point(77,76)

print("a1: ", a1.getPoint())
print("a1: ", a1)
print("a2: ", a2.getPoint())
print("a2: ", a2)
print("a3: ", a3.getPoint())
print("a3: ", a3)
print("a4: ", a4.getPoint())
print("a4: ", a4)
print("a5: ", a5.getPoint())
print("a5: ", a5)
print("a6: ", a6.getPoint())
print("a6: ", a6)
print("a7: ", a7.getPoint())
print("a7: ", a7)

print("changing a4")
a4 = Point(555,555)
print("a1: ", a1.getPoint())
print("a1: ", a1)
print("a2: ", a2.getPoint())
print("a2: ", a2)
print("a3: ", a3.getPoint())
print("a3: ", a3)
print("a4: ", a4.getPoint())
print("a4: ", a4)
print("a5: ", a5.getPoint())
print("a5: ", a5)
print("a6: ", a6.getPoint())
print("a6: ", a6)
print("a7: ", a7.getPoint())
print("a7: ", a7)


print("changing a1")
a1 = Point(999,999)
print("a1: ", a1.getPoint())
print("a1: ", a1)
print("a2: ", a2.getPoint())
print("a2: ", a2)
print("a3: ", a3.getPoint())
print("a3: ", a3)
print("a4: ", a4.getPoint())
print("a4: ", a4)
print("a5: ", a5.getPoint())
print("a5: ", a5)
print("a6: ", a6.getPoint())
print("a6: ", a6)
print("a7: ", a7.getPoint())
print("a7: ", a7)

