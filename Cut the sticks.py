#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    length=len(arr)
    ar=1
    near=[]
    while(ar!=0):
        
        length=len(arr)

        count=0
        if not len(arr):
            break
        
        dec=min(arr)
        near.append(length)
        for i in range(0,length):
            arr[i]=arr[i]-dec
            if(arr[i]==0):
                count=count+1

        for i in range(0,count):
    
            arr.remove(0)

        

    return near
            
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
