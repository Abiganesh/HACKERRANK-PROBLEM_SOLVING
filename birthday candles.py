#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles,maxu):
    for i in candles:
        if(i>maxu):
            maxu=i
    return candles.count(maxu)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    maxu=0;

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles,maxu)

    fptr.write(str(result) + '\n')

    fptr.close()
