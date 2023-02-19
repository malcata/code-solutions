# Enter your code here. Read input from STDIN. Print output to STDOUT


def count_distinct_countries(countries):    
    print(len(set(countries)))

if __name__ == '__main__':
    n = int(input().strip())
    countries = []
    
    for country in range(n):
        countries.append(input())
    
    count_distinct_countries(countries)        
