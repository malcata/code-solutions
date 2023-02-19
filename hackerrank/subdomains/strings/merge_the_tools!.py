
from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here

    # break in chunks
    chunks = [string[i:i+k] for i in range(0, len(string), k)]

    # reduce to unique
    res = [''.join(OrderedDict.fromkeys(i)) for i in chunks]
#    res = [''.join(set(i)) for i in chunks]    
    
    #print results
    [print(i) for i in res]

    
    #print(string, chunks,res)  
    
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)