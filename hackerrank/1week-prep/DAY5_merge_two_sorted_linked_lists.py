#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    #list 1 is empty return the other one
    if head1 == None:
        return head2

    #list 2 is empty return the other one
    if head2 == None:
        return head1
    
    # lowest number first
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
        
    current = head
    n=0

    # while one of the queue as elements
    # add to a new linkedlist     
    while head1 != None or head2 != None:

        #head1 is empty 
        if head1 == None:
            current.next = head2
            break

        #head 2 is empty
        if head2 == None:
            current.next = head1
            break 

        # lowest number first (list 1?)
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else: # definitely list2
            current.next = head2
            head2 = head2.next
            
        current = current.next

    return head
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
