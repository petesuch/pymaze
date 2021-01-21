#!/usr/bin/python3.8

# Is it possible to avoid creating objects with identical values?  I want to create
# a class whose instances will not have the same values. If you create instances with
# the value that have already been used you'll get old same instance.  I did it using
# a special class method:

class A():
    instances = []
    def __init__(self, val):
        self.val = val

    @classmethod
    def new(cls, val):
        # Return instance with same value or create new.
        for ins in cls.instances:
            if ins.val == val:
            return ins

        new_ins = A(val)
        cls.instances.append(new_ins)
        return new_ins

a1 = A.new("x")
a2 = A.new("x")
a3 = A.new("y")
print a1 # <__main__.A instance at 0x05B7FD00>
print a2 # <__main__.A instance at 0x05B7FD00>
print a3 # <__main__.A instance at 0x05B7FD28>

#  Is there a way to do this in a more elegant way without using the .new method?
#
#  raise ValueError("Can't have objects with same values")

#  But, a1 and a2 are essentially two references to the same object, which is
#  unavoidable. Your current code well prevents different objects with same value
#  from being created, but you can't stop an object from having two references.

#  Maybe you can do it with __new__ or __init__ . You could do the new method inside init

#  "prevents different objects with same values from being created " is what i want.
#  Having several references to the same object is ok.

# This can be done by overriding the __new__ method, which is responsible for
# creating new instances of a class. Whenever you create a new instance you store
# it in a dict, and if the dict contains a matching instance then you return it
# instead of creating a new one:


class A:
    instances = {}
    def __new__(cls, val):
        try:
            return cls.instances[val]
        except KeyError:
            pass
        obj = super ().__new__(cls)
        cls.instances[val] = obj
        return obj
    def __init__(self, val):
        self.val = val


a = A(1)
b = A(2)
c = A(1)
print(a is b) # False
print(a is c) # True


# One downside of this solution is that the __init__ method will be called
# regardless of whether the instance is a newly created one or one that has been
# stored in the dict. This can cause problems if your constructor has undesired
# side effects:

class A:
    def __init__(self, val):
        self.val = val
        self.foo = 'foo'

a = A(1)
a.foo = 'bar'
b = A(1)
print(a.foo) # output: foo

# Notice how a 's foo attribute changed from "bar" to "foo" when b was created.
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

# Thanks, it worked for me. You mentioned important thing that i missed:
# Notice how a's foo attribute changed.
# One thing i changed is onelining the __call__ method:

def __call__(cls, arg):
    return cls.instances.setdefault(arg, super(MemoMeta, cls).__call__(arg))

# That's not a good idea. It is hard to read as a single line, and will create a
# new instance every time, and then throws it away. (It creates an instance, that
# instance is passed to setdefault , and if the key already existed in the dict
# then the instance is discarded.)

# You could try functools.lru_cache For example:

from functools import lru_cache
class A:
    @lru_cache()
    def __new__(cls, arg):
        return super().__new__(cls)
    def __init__(self, arg):
        self.n = arg

#Sample usage:
>>> a1 = A('1')
>>> a2 = A('1')
>>> a1 is a2
True

>>> a1.n
'1'
>>> a2.n
'1'

# Alternatively you could try building a custom caching class, as pointed out by
# Raymond Hettinger in this tweet: https://twitter.com/raymondh/status/977613745634471937.
# It's sad that this module doesn't exists in python's 2.7 functools.

# To make it more elegant, implement the duplicate check in __new__ , so it will be
# performed when you call A(something).

# Just do it in __new__ :

def __new__(cls, val=None):
    for i in cls.instances:
        if val == i.val:
            return i
        return object.__new__(cls)

# It's too late in __init__ , a new instance of the class has already been created.
# One optimization would be to change instances to a dictionary mapping values to
# instances since each value should only map to one instance
