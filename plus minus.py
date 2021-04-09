#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zcount=0;
    pcount=0;
    ncount=0;

    

    for i in arr:
        if(i==0):
            zcount=zcount+1
        elif(i>0):
            pcount=pcount+1
        else:
            ncount=ncount+1
    length=len(arr)
    zero=zcount/length
    positive=pcount/length
    negative=ncount/length
    print('%.6f'%positive)
    print('%.6f'%negative)
    print('%.6f'%zero)
    
            
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
