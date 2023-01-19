#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix_old(matrix):
    # Write your code here

    # initialize max sum with sum as is TOP-LEFT
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_sum+=matrix[i][j]
    print(matrix, max_sum)
        
    # if bigger, reverse columns
    # transpose the matrix for easier processing
    transpose = [[matrix[j][i]
        for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix = transpose
            
    for i in range(2*n):
        left,right=0,0
        left = max(matrix[i][:n])
        right = max(matrix[i][n+1:])
        print(i, left, right)
        
        if right > left:
            print("better reverse column", i)
            matrix[i].reverse()

    # transpose back the matrix
    transpose = [[matrix[j][i]
        for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix = transpose
            
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_sum+=matrix[i][j]
    print(matrix,max_sum)

    # if bigger, reverse rows
    for i in range(n):
        left,right=0,0
        left = max(matrix[i][:n])
        right = max(matrix[i][n+1:])

        print(i, left, right)
        
        if right > left:
            print("better reverse row", i)
            matrix[i].reverse()
            
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_sum+=matrix[i][j]
    print(matrix, max_sum)
    
    return max_sum

def flippingMatrix(matrix):
    # Write your code here
    max_sum = 0
    
    # max from corners
    for i in range(n):
        for j in range(n):
            max_sum += max(matrix[i][j], matrix[2*n-1-i][j],matrix[i][2*n-1-j], matrix[2*n-1-i][2*n-1-j])
                        
    return max_sum

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
