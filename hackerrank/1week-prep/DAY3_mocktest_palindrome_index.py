#!/bin/python3

import math
import os
import random
import re
import sys
import logging

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

#similar to its reverse
def palindrome(s):
    return s == s[::-1]
        
# 12/15 tests passed
def palindromeIndex(s):
    l = len(s)
#    logging.warning('palindrome?' + ' ' + s)
        
    if palindrome(s):
        return -1
    elif l>2: # not a palindrome yet
        for i in range(l):
            if s[i] != s[l-1-i] and palindrome(s[:i]+s[i+1:]):
                logging.warning(s[:i]+s[i+1:])
                return i
            else:
                logging.warning(s[i] + ' equals' + s[l-1-i] + '?')

    # either a palindrome or not possible to be a palindrome with a single change
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

