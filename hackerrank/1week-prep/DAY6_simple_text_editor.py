# Enter your code here. Read input from STDIN. Print output to STDOUT#!/bin/python3

import math
import os
import random
import re
import sys
import logging

# 9/16 test cases failed :(
    
def text_editor(ops):

    S, back = '', []    
#    logging.warning(ops)

    # load moment 0, the empty string
    back.append(S)

    for op in ops:
        l=len(op)

#        logging.warning(str(op))
        
        if op[0] == '1' and l == 2:
            S+=op[1]
#            logging.warning('append(1): ' + op[1] + ' => ' + S)
            back.append(S)
        elif op[0] == '2' and l == 2:
            k = int(op[1])
            if len(S)>= k :
                S = S[:-1*k]
#                logging.warning('delete(2): ' + op[1] + ' => ' + S)
                back.append(S)
            else:
                pass
#                logging.warning('ignoring delete')                
        elif op[0] == '3' and l == 2:
            k = int(op[1])
            print(S[k-1])
#            logging.warning('print(3): ' + op[1] + ' => ' + S)
        elif op[0] == '4' and l == 1:
            if len(back)>=2: #restore 
                back.pop()
                S = back[-1]
#                logging.warning('undo(4):' + ' => ' + S)       
            else:
                pass
#                logging.warning('ignoring undo')
        else:
            pass
#            logging.warning('ignoring command')                
               
    return
    

if __name__ == '__main__':

    n = int(input().strip())

    operations = []

    for _ in range(n):
        operations.append(list(map(str, input().rstrip().split())))

    text_editor(operations)
