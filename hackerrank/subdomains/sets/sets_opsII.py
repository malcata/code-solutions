import logging

def run_command(s, command):
    if len(s)<= 0:
        return s
    
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    elif command[0] == 'remove' and len(s.intersection(set({int(command[1])}))) == 1:
        s.remove(int(command[1]))

    return s

if __name__ == '__main__':
    n = int(input()) # get set size
    s = set(map(int, input().split())) # get size

    m = int(input()) # nr commands    

    # get commands
    for  c in range(m):
#        logging.warning(s)
        command = input().rstrip().split()
#        logging.warning(command)
        s = run_command(s,command)

    print(sum(s))