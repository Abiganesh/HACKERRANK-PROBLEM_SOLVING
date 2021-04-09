#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min2=0
    max1=0
    x=len(arr)-1
    y=len(arr)
    for i in range(0,x) :
        min2=min2+arr[i]
    for j in range(1,y):
        max1=max1+arr[j]
    print(str(min2)+' '+str(max1))        
            

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
