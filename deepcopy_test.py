#!/usr/bin/python3.7
#
#  experiments comparing copy and deepcopy

import copy

print("******************************")
a = "PETER SUCHSLAND"
b = 1, 2, 3, 4
c = [1, 2, 3, 4]
d = [1,2,[3,[4],[[5],[6,7,8],[9,10],a,b],c]]

a1 = copy.copy(a)
b1 = copy.copy(b)
c1 = copy.copy(c)
d1 = copy.copy(d)

print("copy.copy")

print("id(a):", id(a))
print("id(a1):", id(a1))
print("id(b):", id(b))
print("id(b1):", id(b1))
print("id(c):", id(c))
print("id(c1):", id(c1))
print("id(d):", id(d))
print("id(d1):", id(d1))

print("******************************")
print("id(a)==id(a1)", id(a) == id(a1))
print("id(b)==id(b1)", id(b) == id(b1))
print("id(c)==id(c1)", id(c) == id(c1))
print("id(d)==id(d1)", id(d) == id(d1))

print("******************************")

print("copy.deepcopy")
a2 = copy.deepcopy(a)
b2 = copy.deepcopy(b)
c2 = copy.deepcopy(c)
d2 = copy.deepcopy(d)


print("id(a):", id(a))
print("id(a2):", id(a2))
print("id(b):", id(b))
print("id(b2):", id(b2))
print("id(c):", id(c))
print("id(c2):", id(c2))
print("id(d):", id(d))
print("id(d2):", id(d2))

print("id(a)==id(a2)", id(a) == id(a2))
print("id(b)==id(b2)", id(b) == id(b2))
print("id(c)==id(c2)", id(c) == id(c2))
print("id(d)==id(d2)", id(d) == id(d2))

print("******************************")

print("******************************")
print ("now: aa = [1,2,3,4]")
print ("now: bb = aa")
aa = [1,2,3,4]
bb = aa
print("Memory ID of `aa` ", id(aa))
print("Memory ID of `bb` ", id(bb))
print("change: b[0] ")
bb[0] = 1000
print(aa)
# [1000, 2, 3, 4]
print(bb)
# [1000, 2, 3, 4



print("******************************")

ddd = {1: "one", 2: "two"}
aaa = [1,2,3,4, ddd]
bbb = copy.copy(aaa)
#
# Now change the contents of d
aaa[0] = 1000
ddd[3] = "three"
print("Contents of `aaa`", aaa)

# Contents of `a` [1000, 2, 3, 4, {1: 'one', 2: 'two', 3: 'three'}]
print("Contents of `bbb`", bbb)

# Contents of `b` [1, 2, 3, 4, {1: 'one', 2: 'two', 3: 'three'}]
print("Memory ID of A `aaa` ", id(aaa))
print("Memory ID of A `bbb` ", id(bbb))
print("******************************")

d = {1: "one", 2: "two"}
a = [1,2,3,4, d]
b = copy.deepcopy(a)
#
# Now change the contents of d
a[0] = 1000
d[3] = "three"
print("Contents of `a`", a)
print("Contents of `b`", b)

print("******************************")
print("Memory ID of `d` ", id(d))
print("Memory ID of  `a` ", id(a))
print("******************************")
