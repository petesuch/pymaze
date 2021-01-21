#!/usr/bin/python3.8

####################################################################################
#   tupleexpansion.py
#
#   A recursive function to expand and beautify nested tuples into pairs
#
#   Peter Suchsland
#   January 2021
####################################################################################
def te(t):
    groupings = 2   ### 1 or 2
    lst = []
    newlst = []

    def recursiveexpand(t):
        for element in t:
            if (isinstance(element, tuple)):
                recursiveexpand(element)

            if ( (isinstance(element,int)) or
                    (isinstance(element,str)) or
                    (isinstance(element,float))) :
                lst.append(element)


    recursiveexpand(t)

    if groupings == 1:
        len = (lst.__len__())
        for i in range(len):
            newlst.append( (lst[i]) )

    if groupings == 2:
        len = (lst.__len__())/2
        len = int(len)
        for i in range(len):
            newlst.append( (lst[2*i],lst[2*i+1]) )

    #print(tuple(newlst))
    return tuple(newlst)

###################################################################################
#  Testing
###################################################################################

a=1;b=2;c=3;d=4;e=6;f=7
v1 = (a,b)
v2 = (a,c)
v3 = (c,e)
tp1 = v1,v2
## nested tuples:
tp2 = ((((((31, "cat"), (2, "dog")), (25, 38.2))), (77, 6.6)), (44, 33))
tp3 = tp2,tp1,tp2 ### a total nested mess !!!

#print(t2+v1) #print(t1,v1) #print(t1+v1) #print(v1,v2) #print(v1+v2)

print("original Tuple: ")
print(tp3)
print("After Tuple Expansion: ")
print(te(tp3))
print("original Tuple: ")
print(v1)
print("After Tuple Expansion: ")
print(te(v1))

####################################################################################
