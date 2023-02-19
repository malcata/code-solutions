# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging


def run_command(command,set1, set2):
    
#    logging.warning(command)

    if command == 'intersection_update':
        set1.intersection_update(set2)
    elif command == 'update':
        set1.update(set2)
    elif command == 'difference_update':
        set1.difference_update(set2)
    elif command == 'symmetric_difference_update':
        set1.symmetric_difference_update(set2)
 
#    logging.warning(set1)
    return set1    

if __name__ == '__main__':
    n = int(input()) # nr elements set A
    a = set(map(int, input().split())) # set A
#    logging.warning(a)    
    
    t = int(input()) # nr of other sets

    # get other sets
    for s in range(t):
        command = list(map(str, input().split())) # command + nr elements set    
        b = set(map(int, input().split())) # set B
        a = run_command(command[0],a,b)
        
    print(sum(a))