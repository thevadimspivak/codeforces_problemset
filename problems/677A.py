l1 = [int(i) for i in input().split()]
n = l1[0]
h = l1[1]
l2 = [int(i) for i in input().split()]

r = 0

for j in range(n):
    if l2[j] <= h:
        r += 1
    else:
        r += 2


print(r)
