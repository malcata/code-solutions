# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging

def check_subset(s1, s2):
    
    if len(s1|s2) == max(len(s1),len(s2)) and len(s1)<=len(s2):
         print(True)
    else:
        print(False)

if __name__ == '__main__':
    n = int(input()) # nr test cases


    # get test cases
    for  t in range(n):
        ma = int(input()) # nr elements set A    
        a = set(map(int, input().split())) # set A
        mb = int(input()) # nr elements set B    
        b = set(map(int, input().split())) # set B
        check_subset(a,b)