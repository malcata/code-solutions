# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == '__main__':    
    ab = int(input().rstrip())
    bc = int(input().rstrip())
    
    angle = math.atan(ab/bc)
    print(str(round(math.degrees(angle)))+'\N{DEGREE SIGN}')
