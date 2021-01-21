#!/usr/bin/python3.8

#
#   addbud and addbranch subroutines examined for testing and understanding
#

# since I need a dictionary that provides lifo ... apparently I need an ordereddict

### Global variables:

import collections
germdict = collections.OrderedDict()
germ = ''

###################################################################################
### tuple expand
def te(t):
    lst=[]
    newlst =[]
    def re(t): ### recursive expand
        for element in t:
            if isinstance(element, tuple) :
                re(element)
            if isinstance(element, int) :
                lst.append(element)

    re(t)
    ### for grouping
    len = (lst.__len__())/2
    len = int(len)
    #print("After Tuple Expansion: ")
    for i in range(len):
        newlst.append( (lst[2*i],lst[2*i+1]) )

    return(tuple(newlst))
###################################################################################
def addbud(x,y,a,b):
    germ = "G"+str(x)+"_"+str(y)
    if (germdict.__contains__(germ)):
        val = germdict[germ]
        germdict[germ] = te((val,(a,b)))
        print("germdict", germdict)
    else:
        exec("%s = []" % germ)
        germdict[germ] = te((a,b))
        print("germdict", germdict)

def popGetXY():
    if (germdict.__len__() > 0):
        val = germdict.popitem(last=True)
        if ( (val.__len__() > 1) and (val[1].__len__() > 0 )) :
            print("val[0]: ",val[0])
            print("val[1]: ",val[1])
            lsv = list(val[1])
            (x,y) = lsv.pop()
            if lsv.__len__() > 0:
                germdict[val[0]] = tuple(lsv)
            print("lastgermdict", germdict)
            return (x,y)
        else:
            return False
    else:
        return False

###################################################################################
# testing
###################################################################################

addbud(11,1,3,4)
addbud(11,1,7,8)
addbud(11,1,11,12)
addbud(2,4,3,4)
addbud(2,4,7,8)
addbud(2,4,11,12)
addbud(3,2,3,4)
addbud(3,2,5,6)
#addbud(3,2,7,8)
addbud(4,14,3,4)
#addbud(4,14,7,8)
#addbud(4,14,11,12)
print(germdict)
#print(germdict["G4_14"][1][0])
#val = germdict.popitem(last=True)
#print("val: ", val, " type: ", type(val))
#print("length of val: " , val.__len__())
#print("length of val[1]: " , val[1].__len__())
print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass


print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)

try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)
try:
    (x,y) = popGetXY()
    print("x:",x)
    print("y:",y)
except:
    print ("...empty...")
    pass

print(germdict)










#print("val[0] ", val[0], " val[1]: ", val[1] )
#print("val[1][0] ", val[1][0], " val[1][1]: ", val[1][1] )
#print("val[1][0][0] ", val[1][0][0], " val[1][1][0]: ", val[1][1][0] )

#print(popbud())
#desired : (11,12)
#print(popbud())
#print(popbud())
#desired : (7,8)
#print(popbud())
#desired : (3,4)
#desired : ??





"""
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
#(x,y) = getVals(val)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
#(x,y) = getVals(val)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)
print(germdict)
(x,y) = popGetXY()
print("x:",x)
print("y:",y)

print "Array $germ contains the following points: (@$germ)\n";
print "The value of $germ\t: (@$germ)\n";
my $temp = pop @$germ;
my ($xnew, $ynew) = split(/\,/, $temp);
print "Array $germ contains the following points: (@$germ)\n";
print "Array $germ contains the following points: (@$germ)\n";
my $temp = pop @$germ;
my ($xnew, $ynew) = split(/\,/, $temp);
print "Array $germ contains the following points: (@$germ)\n";
print "The value of $germ:(@$germ)\n";
#sub addbud()
#{
    #$germ= "G$_[0]$_[1]";
    #print "1\t: $germ\n";

    #if ( @$germ) {
        push @$germ, "$_[2],$_[3]";
        print "2\t: $germ\n";
    }
    else {
        @$germ= ( "$_[2],$_[3]" );
        print "3\t: $germ\n";
    }
}
"""

