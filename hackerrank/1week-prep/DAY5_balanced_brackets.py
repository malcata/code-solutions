#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
import logging

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    queue = deque() 
    l = len(s)
    
    # cannot start by closing
#    if s[0] == ')' or s[0]=='}' or s[0]==']':
#        return 'NO'    
    
    # must be in pairs and exist
#    if s == None or l%2 != 0:
#        return 'NO'
    
#    logging.warning(s + ' ' + str(l))    
#    logging.warning(list(queue))
    
    for c in s:            
        l = len(queue)

        if c == '(' or c=='{' or c=='[':
            queue.append(c)
        elif c == ')' and l>0 and queue[-1] == '(':
            queue.pop()
        elif c == '}' and l>0 and queue[-1] == '{':
            queue.pop()
        elif c == ']' and l>0 and queue[-1] == '[':
            queue.pop()
        else: 
            return 'NO'    

    if len(queue)==0: 
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
