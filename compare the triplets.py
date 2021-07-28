#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b,al,bl):
    length=len(a)
    for i in range(0,length):
        if(a[i]>b[i]):
            al=al+1
        elif(a[i]<b[i]):
            bl=bl+1
        else:
            cl=0
    return str(al)+str(bl)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    al=0
    bl=0
    
    
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b,al,bl)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
