n = int(input())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
p = s1[0]
q = s2[0]

l = s1[1:] + s2[1:]
d = list(dict.fromkeys(l))
if len(d) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')