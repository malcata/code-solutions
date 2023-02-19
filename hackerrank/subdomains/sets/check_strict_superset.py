# Enter your code here. Read input from STDIN. Print output to STDOUT

def strict_super_set(set1, set2):
    if len(set1|set2) == len(set1) and len(set1)>len(set2):
        return True
    else:
        return False  

if __name__ == '__main__':
    a = set(map(int, input().split())) # set A
    res = True
    
    #    logging.warning(a)    
    
    n = int(input()) # nr of other sets

    # get other sets
    for s in range(n):
        b = set(map(int, input().split())) # set B
        res = res and strict_super_set(a, b)

    print(res)