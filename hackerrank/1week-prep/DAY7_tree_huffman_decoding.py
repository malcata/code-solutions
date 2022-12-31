import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging

def process_node(root,node,s):    
    res = ''

#    s.strip()
    
#    logging.warning('alpha? ' + str(node.data.isalpha()) + ' ' + str(node.freq))
    
    if node.data.isalnum() or node.data in ['?','!',',','.']: # leave
        logging.warning('leave=' + node.data + '=evael')
        res += node.data
        if len(s)>=1: # decode next start in root
            logging.warning('next = ' + s)
            res += process_node(root, root,s)
    elif len(s)>= 1 and s[0] == '0' : # not a leave take a left
        logging.warning('go left = ' + s[0])
        res += process_node(root,node.left,s[1:])
    elif len(s)>= 1 and s[0] == '1' : # not a leave take a right
        logging.warning('go right = ' + s[0])
        res += process_node(root,node.right,s[1:])
        
    return res

def decodeHuff(root, s):
        
    if s.isalpha():
        print(s)
    else:
        print(process_node(root,root,s))
    
    
ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)


