#!/usr/bin/python3.8
#
#   A Class that does not allow multiple instances to have identical values.
#   Attempts to create new objects with the same values are returned the first
#   original instance.
#
###################################################################################

class Nodup:
    __instances = {}
    def __new__(cls,val):

        if ( cls.__instances.__contains__(val) ) :
            return cls.__instances.__getitem__(val)

        obj = super().__new__(cls)
        cls.__instances[val] = obj
        return obj

    def __init__(self, val) :
        self.__val = val
        self.__name="Name:"+str(self.__val)

    def getName(self) :
        return (self.__name)

    def setName(self,name ) :
        self.__name="Name:"+str(name)



n1 = Nodup(11)
n2 = Nodup(11)
n3 = Nodup(11)
n4 = Nodup(11)
n5 = Nodup(11)
n6 = Nodup(11)
n7 = Nodup(11)
n8 = Nodup(11)
n9 = Nodup(33)
n99 = Nodup(33)

#n1.__val=33
n1.__val=22

# Whats the point of creating all this code if it doesn't get hidden?
# SOLVED ... just use double underscore.

#print (n1.__val)
#print (n1.setName("blinkblank"))
#print (n1.hello)
print (n1.getName(),":", n1)
print (n2.getName(),":", n2)
print (n3.getName(),":", n3)
print (n4.getName(),":", n4)

print (n4.getName(),":", n4)
print (n5.getName(),":", n5)
print (n6.getName(),":", n6)
print (n7.getName(),":", n7)



"""
try:
    obj = cls.__instances[val]
    return obj
except KeyError:
    pass
"""

