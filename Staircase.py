#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    j=1
    for i in range(n,0,-1):
        a=" "*(i-1)
        
        print(a+"#"*j)
        j+=1
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
