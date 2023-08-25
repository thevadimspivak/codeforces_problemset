n = int(input())
l = []

for line in range(n):
    x = input()
    l.append(x)

t1 = l[0]
t2 = ''

for i in l:
    if i != t1:
        t2 = i
        break

if l.count(t1) > l.count(t2):
    print(t1)
else:
    print(t2)
    