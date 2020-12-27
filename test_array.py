#!/usr/bin/python3.7
import math
import random
myvar = 10
myarr = [[0 for i in range(myvar)] for j in range(myvar)]

for i in range(myvar):
    for j in range(myvar):
        myarr[i][j]=i*j
        #myarr[i][j]=random.random()*100


for i in range(myvar):
    for j in range(myvar):
        if j == myvar-1:
            print(myarr[i][j])
        else:    
            print(myarr[i][j],end ='\t')
