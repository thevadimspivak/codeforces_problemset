n = int(input())
s = [i for i in input()]

a = 0
d = 0
for i in range(len(s)):
    if s[i].count('A'): a += 1
    elif s[i].count('D'): d += 1

if a > d:
    print('Anton')
elif a == d:
    print('Friendship')
else:
    print('Danik')
