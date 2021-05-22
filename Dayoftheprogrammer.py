#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    
    if(year % 4) == 0:
    # check if year is divisible by 100
        if(year %100) == 0:
        # check if year is divisible by 400
            if(year % 400) == 0:
                a=12
            else:
            # year is divisible by 100 but not by 400
                a=13
        else:
        # year is divisible by 4 but not by 100
            a=12
    else:
    # year is not divisible by 4
        a=13
    
    b=str(a)
    c=str(year)
    output=b+".09."+c
    return output
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
