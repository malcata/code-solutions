#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#



def caesarCipher(s, k):
    # Write your code here

    alphaLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphaUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    encrypted = ''
    
    # shift by k
    for letter in s:
        if letter in alphaLower:
            encrypted+= alphaLower[int(math.remainder(alphaLower.index(letter)+k,26))]
        elif letter in alphaUpper:
            encrypted+= alphaUpper[int(math.remainder(alphaUpper.index(letter)+k,26))]
        else:
            encrypted += letter
        
    # return encrypted string    
    return encrypted 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
