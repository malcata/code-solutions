# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging

def symmetric_difference(set1, set2):
    res = list(set1 ^ set2)
    res.sort()

    return res

if __name__ == '__main__':
    n = 0
    set1, set2 = {},{}
    result = []

    n = int(input())
    set1 = set(map(int, input().split()))

    n = int(input())
    set2 = set(map(int, input().split()))

    result = symmetric_difference(set1,set2)
    
    print(*result, sep="\n")

