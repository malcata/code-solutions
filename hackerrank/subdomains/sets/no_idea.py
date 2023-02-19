# Enter your code here. Read input from STDIN. Print output to STDOUT

def calc_happiness(arr,a,b):
    happy = 0
    
    for n in arr:
        if n in a:
            happy += 1
        elif n in b:
            happy += -1
    
    print(happy)


if __name__ == '__main__':
    n, m = (int, input().split()) # 
    arr = list(map(int, input().split()))
    a = set(map(int, input().split())) # set A
    b = set(map(int, input().split())) # set B
    
    calc_happiness(arr,a,b)
    
    