### tupleexpand
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
def addbud(__x,__y,a,b):
    germ = "G"+str(__x)+'_'+str(__y)
    if (germdict.__contains__(germ)):
        val = germdict[germ]
        germdict[germ] = te((val,(a,b)))
    else:
        exec("%s = []" % germ)
        germdict[germ] = te((a,b))
###################################################################################

def popGetXY():
    print("1germdict:", germdict)
    if (germdict.__len__() > 0):
        val = germdict.popitem(last=True)
        if ( (val.__len__() > 1) and (val[1].__len__() > 0 )) :
            print("val[0]: ",val[0])
            print("val[1]: ",val[1])
            lsv = (val[1])
            print("lsv: ", lsv)
            myx, myy = lsv.pop()
            print("x, y: ", myx, myy)
            if lsv.__len__() > 0:
                germdict[val[0]] = tuple(lsv)
            #print("lastgermdict", germdict)
            print("2germdict:", germdict)
            return (myx,myy)
        else:
            return False
    else:
        return False


