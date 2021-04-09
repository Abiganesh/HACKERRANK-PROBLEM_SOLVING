#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#

def timeConversions(s):
    div=""
    forma=""
    for i in s:
        if(len(div)>7):
            forma+=i
        else:
            div+=i
    if(forma=="PM"):
        hour=""
        minu=""
        for i in div:
            if(len(hour)>1):
                minu+=i
            else:
                hour+=i
        if(hour=="12"):
            hour="12"
            final1=hour
        else:
            final1=int(hour)+12
        final=str(final1)+minu
        
    else:
        hour=""
        minu=""
        for i in div:
            if(len(hour)>1):
                minu+=i
            else:
                hour+=i
        if(hour=="12"):
            hour="00"
            final1=hour
        else:
            final1=hour
        final=final1+minu
    return final 
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversions(s)

    f.write(result + '\n')

    f.close()
