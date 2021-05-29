#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n,count):
    number=str(n)
    for i in number:
        i=int(i)
        try:
            if(n%i==0):
                print(i)
                count=count+1
        except ZeroDivisionError:
            a=0
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        count=0

        result = findDigits(n,count)

        fptr.write(str(result) + '\n')

    fptr.close()

