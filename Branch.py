#!/usr/bin/python
#
#   I want to have a class of data structure that is similar to a list and set.
#   It must prevent identical coordinates from being added, It must provide LIFO
#   popping and pushing.  It should return a negative int or False when garbage is
#   entered or when popped beyond the last element.

class Branch:

    def __init__(self):
        self.set = set() # has a set
        self.lst = [] # has a list

    def push(self, x, y):
        self._x = x
        self._y = y

        len1 = self.set.__len__()
        value = self.set.add( (self._x, self._y) )
        print("value: ", value)
        len2 = self.set.__len__()
        if (len1 < len2):  # if the set gets larger, add the new point
            self.lst.append((self._x,self._y))

    def pop(self):
        if self.lst.__len__() > 0:
            value = self.lst.pop()
            self.set.remove(value)
            return (value)
        else:
            return False

    def printBranch(self):
        if self.lst.__len__() > 0:
            for item in self.lst:
                print(item)
        else:
            return False


# testing...

b1 = Branch();
b1.push(1,1)
b1.push(1,1)
b1.push(2,2)
b1.push(2,2)
b1.push(1,1)
b1.push(4,1)
b1.push(3,1)
b1.push(3,1)
b1.push(3,3)
b1.push(3,4)
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
print("...")
b1.pop()
b1.printBranch()
print("...")
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
#print("...")
b1.pop()
b1.printBranch()
b1.push(1,1)
b1.push(1,1)
b1.push(2,2)
b1.push(2,2)
b1.push(1,1)
b1.push(4,1)
b1.push(3,1)
b1.push(3,1)
b1.push(3,3)
b1.push(3,4)
b1.printBranch()
b1 = Branch();
b1.push(1,1)
b1.push(1,1)
b1.push(2,2)
b1.push(2,2)
b1.push(1,1)
b1.push(4,1)
b1.push(3,1)
b1.push(3,1)
b1.push(3,3)
b1.push(3,4)
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.push(1,1)
b1.push(1,1)
b1.push(2,2)
b1.push(2,2)
b1.push(1,1)
b1.push(4,1)
b1.push(3,1)
b1.push(3,1)
b1.push(3,3)
b1.push(3,4)
b1.pop()
b1.printBranch()

b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.printBranch()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()
b1.pop()

