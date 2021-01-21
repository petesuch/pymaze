#!/usr/bin/python
#
# Another option is to use a metaclass and override its __call__ method:

class MemoMeta(type):
    def __new__(mcs, name, bases, attrs):
        cls = super ().__new__(mcs, name, bases, attrs)
        cls.instances = {}
        return cls
    def __call__(cls, val):
        try:
            return cls.instances[val]
        except KeyError:
            pass
        obj = super ().__call__(val)
        cls.instances[val] = obj
        return obj

class A(metaclass=MemoMeta):
    def __init__(self, val):
        self.val = val
        self.foo = 'foo'

# This bypasses the problem with __init__ being called on existing instances:
a = A(1)
a.foo = 'bar'
b = A(1)
print(a.foo) # output: bar

###################################################################################
#   Point.py
#
#   A Class that does not allow multiple instances to have identical values.
#   Attempts to create new objects with the same values are returned the first
#   original instance.
#
###################################################################################
class Point:
    instances = {}
    def __new__(cls, val1, val2):
        try:
            obj_adr = cls.instances[val1,val2]
            return obj_adr
        except KeyError:
            pass

        obj = super ().__new__(cls)
        cls.instances[val1,val2] = obj
        print("cls: ", cls, " obj: ", obj)
        return obj

    def __init__(self, val1,val2):
        print("self: ", self)
        self.val1 = val1
        self.val2 = val2

    def getX(self):
        return self.val1
    def getY(self):
        return self.val2
    def getPoint(self):
        return (self.val1, self.val2)


p1 = Point(1,1)
print("p1: ", p1.getPoint())
print("p1: ", p1)
p2 = Point(2,2)
print("p2: ", p2.getPoint())
print("p2: ", p2)
p3 = Point(1,1)
print("p3: ", p3.getPoint())
print("p3: ", p3)
p4 = Point(1,1)
print("p4: ", p4.getPoint())
p5 = Point(5,5)
print("p4: ", p4)
p5 = Point(5,5)
a6 = Point(5,5)
a7 = Point(77,76)

print("p5: ", p5.getPoint())
print("p5: ", p5)
print("a6: ", a6.getPoint())
print("a6: ", a6)
print("a7: ", a7.getPoint())
print("a7: ", a7)

print("changing p4")
p4 = Point(555,555)
print("p1: ", p1.getPoint())
print("p1: ", p1)
print("p2: ", p2.getPoint())
print("p2: ", p2)
print("p3: ", p3.getPoint())
print("p3: ", p3)
print("p4: ", p4.getPoint())
print("p4: ", p4)
print("p5: ", p5.getPoint())
print("p5: ", p5)
print("a6: ", a6.getPoint())
print("a6: ", a6)
print("a7: ", a7.getPoint())
print("a7: ", a7)


print("changing p1")
p1 = Point(999,999)
print("p1: ", p1.getPoint())
print("p1: ", p1)
print("p2: ", p2.getPoint())
print("p2: ", p2)
print("p3: ", p3.getPoint())
print("p3: ", p3)
print("p4: ", p4.getPoint())
print("p4: ", p4)
print("p5: ", p5.getPoint())
print("p5: ", p5)
print("a6: ", a6.getPoint())
print("a6: ", a6)
print("a7: ", a7.getPoint())
print("a7: ", a7)

