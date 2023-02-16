

# Stuart starts words with consonants
# Kevin starts words with vowels 

import logging

def extract_chars(string):
    vowels_ref = ['A','E','I','O','U']
    vowels = []
    consonants = []

    for c in string:
            if c in vowels_ref:
                vowels += c
#            else:
#                consonants += c
    return (list(set(vowels))), (list(set(consonants)))

def count_substrings(string, vowels, consonants):
#    substr_kevin, substr_stuart = [],[]
    score_kevin, score_stuart = 0,0 
    
# the real thing without performance
#    for i in range(len(string)):
#        for n in range(i,len(string)):
#            if string[i] in vowels:
##                substr_kevin.append(string[i:n+1])
#                score_kevin += 1                
#            else:
##                substr_stuart.append(string[i:n+1])
#                score_stuart += 1

# the short version
    for i in range(len(string)):
        if string[i] in vowels:
            score_kevin += len(string)-i
        else:
            score_stuart += len(string)-i                
                
#    return(substr_kevin, substr_stuart)       
    return(score_kevin, score_stuart)       
    
def minion_game(string):
    # your code goes here
    vowels, consonants = [],[] 
    substr_kevin, substr_stuart = [], []
    score_kevin, score_stuart = 0,0 
    
    
    # extract vowels
    # extract consonants
    vowels, consonants = extract_chars(string)

#    logging.warning(vowels)
#    logging.warning(consonants)
    
    # generate vowels starting words    
    # generate consonants starting words
    # score

#    substr_kevin, substr_stuart = generate_substrings(string, vowels, consonants)
    score_kevin, score_stuart = count_substrings(string, vowels, consonants)

#    logging.warning(substr_kevin)
#    logging.warning(substr_stuart)    
    
#    logging.warning(score_kevin)
#    logging.warning(score_stuart)    

    # print results    
    if score_kevin == score_stuart :
        print('Draw')
    elif score_kevin > score_stuart:
        print ('Kevin ' + str(score_kevin))
    else:
        print ('Stuart ' + str(score_stuart))    
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)