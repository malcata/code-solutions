
# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging

def count_non_overlap(english, french):
    return(len(set(english)^set(french)))

def count_only_on_first(english, french):
    return(len(set(english)-set(french)))    

def count_intersection(english, french):
    return(len(set(english) & set(french)))    

def count_union(english, french):
    return(len(set(english) | set(french)))    
    
    
if __name__ == '__main__':
    n = int(input())
    english = list(map(int, input().split()))

    n = int(input())
    french = list(map(int, input().split()))

    logging.warning(english)
    logging.warning(french)
        
#    print(count_non_overlap(english, french))
#    print(count_only_on_first(english, french))
#    print(count_intersection(english, french))
    print(count_union(english, french))
