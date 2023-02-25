for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round(i*10**(i-1) + i*10**(i-2) + i*10**(i-3) + i*10**(i-4) + i*10**(i-5) + (i*10**(i-6)).__trunc__() + (i*10**(i-7)).__trunc__() + (i*10**(i-8)).__trunc__() + (i*10**(i-9)).__trunc__()))

# cannot use str
# the right approach should have been by using https://mathworld.wolfram.com/Repunit.html