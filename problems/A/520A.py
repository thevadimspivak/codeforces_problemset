import string

n = int(input())
s = input().lower()

abc = list(string.ascii_lowercase)

s1 = list(dict.fromkeys(list(s)))
s1.sort()

if ''.join(s1) == ''.join(abc):
    print('YES')
else:
    print('NO')