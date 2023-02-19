# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging
from collections import Counter

def captain_room (size, tourists):
    counter_dict = Counter(tourists)    
    
    logging.warning(counter_dict)

    for room, counter in counter_dict.items():
        if counter == 1:
            print(room)

if __name__ == '__main__':
    n = int(input()) # nr elements per group
    tourists = list(map(int, input().split())) # total elements

    captain_room (n, tourists)
    