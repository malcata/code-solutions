#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
import logging


# FIFO QUEUE
# 2 stacks the queue stack and the dequeue stack


class BasicQueue:
    def __init__(self):
        self.s = deque() 
            
    def enqueue(self, element):
        self.s.append(element)
        
    def dequeue(self):
        self.s.popleft()
        
    def print_queue(self):
        print(self.s[0])
                

def runqueue(commands):
#    print(commands)
#    logging.warning(commands)

    myqueue = BasicQueue()
    
    for q in commands:
        if int(q[0]) == 1:
 #           logging.warning('enqueue')
            myqueue.enqueue(q[2:])
#            logging.warning(myqueue.s)
        elif int(q[0]) == 2:
#            logging.warning('dequeue')
            myqueue.dequeue()
#            logging.warning(myqueue.s)
        elif int(q[0]) == 3:
#            logging.warning('print')
            myqueue.print_queue()
 
#    logging.warning(myqueue.s)
            
if __name__ == '__main__':
    q = int(input().strip())

    commands = []
    
    for q_itr in range(q):
        t = str(input().strip())
        commands.append(t)    
            
    runqueue(commands)