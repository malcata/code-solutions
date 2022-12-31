#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # variable inizialization
    pos=0
    neg=0
    zero=0
    
    if n > 100: # Error
        raise Exception("Invalid array size")
    
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        else:
            zero += 1
    
    print(format(pos/n,'.6f'))
    print(format(neg/n,'.6f'))
    print(format(zero/n,'.6f'))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

