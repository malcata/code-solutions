import logging

def line_length(size):
    return (size-1)*4+1    

def gen_string(size, n):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']     
    string = ""

    #left side
    for i in range(size-(size-n)+1):
        if i == 0:
            string += alphabet[size-i-1]
        else:
            string += "-" + alphabet[size-i-1] 
    
    string2 = string[:len(string)-1]
    string += string2[::-1]
            
    logging.warning(string)
            
    return string
    
    
def print_rangoli(size):
    # your code goes here
    n = 2*size-1
    m = line_length(size)
    res = []        
    
    # generate top    
    for i in range(size):
        res.append(gen_string(size,i).center(m,'-'))
    
    # generate bottom (mirror from top)
    for i in range(len(res)-2,-1,-1):
        res.append(res[i])
    
    # print all 
    for i in res:
        print(i)
    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)