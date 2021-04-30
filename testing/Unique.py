#!/usr/bin/python3.8

class P():
    instances = []
    def __init__(self,val1,val2 ):
        self.val1 = val1
        self.val2 = val2

    @classmethod
    def new(cls, val1, val2):
        # Return instance with same value or create new.
        for ins in cls.instances:
            if ((ins.val1 == val1) and (ins.val2 == val2)) :
                return ins

        new_ins = P(val1,val2)
        cls.instances.append(new_ins)
        return new_ins

p1 = P.new(1,2)
print("p1: ", p1)
p2 = P.new(1,2)
print("p2: ", p2)

p3 = P(3,4)
print("p3: ", p3)
p3 = P(3,4)
print("p3: ", p3)
