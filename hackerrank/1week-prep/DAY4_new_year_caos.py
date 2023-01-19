#!/bin/python3

import math
import os
import random
import re
import sys


import logging
from collections import defaultdict

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def minimumBribes(q):

    bribes = {} 
    bribes = defaultdict(lambda:0,bribes)  
    
    while q != sorted(q):
        for i in range(len(q)):
#            logging.warning(q)
            n=i
            while n+1<len(q) and q[n+1] < q[n]:
                bribes[q[n]] += 1
                swapPositions(q,n,n+1)
                n+= 1
#        logging.warning(bribes)    
            
    # exit conditions
#    logging.warning(bribes)    

    if max(bribes.values())>2:
        print('Too chaotic')
    else:
        print(sum(bribes.values()))    

    
######################## v1 ######################
##  8 / 12  sucessful tests
def minimumBribesOLD(q):
    bribes =0

#    logging.warning(str(n) + ' ' + str(q))
    
    for i in range(n-1):
        # short answer
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return

        # count all the people later in queue that have a lower sticker
        bribes += sum(j < q[i] for j in q[i+1:])
#        bribes += sum(map(lambda x : x < q[i], q[i+1:]))
                           
    print(bribes)
    return    
    
    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
