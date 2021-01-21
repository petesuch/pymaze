#!/usr/bin/python3.8
#
# trying to use set... not working or finished yet.
#   I want to create a Point class that prevents instances with identical values
#   from being created without the use of new.

class P():
    instances = set()

    def __init__(self,val1,val2 ):
        if hasprev(val1,val2):
            self.val1 = val1
            self.val2 = val2

    def hasprev(ckself, val1, val2):
        # Return instance with same value or create new.
        for ins in instances:
            if ((ins.val1 == val1) and (ins.val2 == val2)) :
                return ins

        new_ins = P(val1,val2)
        cls.instances.append(new_ins)
        return new_ins

p1 = P.new(1,2)
p2 = P.new(1,2)
p3 = P(3,4)
print("p3: ", p3)
p3 = P(3,4)
print("p3: ", p3)
p3 = P(3,4)
print("p3: ", p3)

print("p1: ", p1)
print("p2: ", p2)
print("p3: ", p3)
