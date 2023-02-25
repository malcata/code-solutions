for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also    
    print(round(((10**i-1)/9)**2))

# cannot use str
#    print(int(str(1)*i)**2)
# the right approach should have been by using https://mathworld.wolfram.com/Repunit.html
