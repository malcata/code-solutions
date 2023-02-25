# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging
import math
import cmath

if __name__ == '__main__':    
    z = input().rstrip()
    z = complex(z)

    # there is an easier way using cmath 
    r = math.sqrt(z.real**2+z.imag**2) 
    phi = cmath.phase(z) 
        
    print(r)
    print(phi)
    