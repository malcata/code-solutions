#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
       
    res='YES' #default

    # sort rows
    for idx, row in enumerate(grid):
#        print(idx)
#        print(row)
        grid[idx] = sorted(row)

#        print('The grid:', grid)
        
    # check if columns are sorted   
    # create transpose grid
    transposeGrid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
#    print('The transpose grid:', transposeGrid)

    # check transpose grid
    for row in transposeGrid:
        if row != sorted(row):
            res = 'NO'
            return res
                
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
