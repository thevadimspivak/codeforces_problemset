n = int(input())
s = input().split()

def f(s):
    print(s.count('1'))
    return 'HARD' if s.count('1') != 0 else 'EASY'


print(f(s))


    
