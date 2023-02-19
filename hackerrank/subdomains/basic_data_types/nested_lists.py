def sortsub(sub_li):
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[1])
    return sub_li

def minsub(sub_li):
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.min(key = lambda x: x[1])
    return sub_li
        
def runner_ups (grades):

    res = []
    if len(grades) >= 1:
        sorted_grades = sortsub(grades)
        minimum = sorted_grades[0][1]
    else: return
    
    while len(sorted_grades) >= 1 and sorted_grades[0][1] == minimum:
        sorted_grades.pop(0)
    
    secmin = sorted_grades[0][1]
    
    while len(sorted_grades) >= 1 and sorted_grades[0][1] == secmin:
        res.append(sorted_grades[0][0])
        sorted_grades.pop(0)    

    res.sort()  
    
    for name in res:
        print(name)      
    
    return
    
if __name__ == '__main__':

    grades = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])
    
    runner_ups(grades)