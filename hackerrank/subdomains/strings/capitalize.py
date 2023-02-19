#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
   
    res = [i.capitalize() for i in s.split(' ')]
        
    return ' '.join(res)

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
