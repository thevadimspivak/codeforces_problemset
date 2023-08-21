""" n, k = map(int, input().split())
l = []
l2 = []
l3 = []
t = 1
for i in range(n):
    if t % 2 != 0:
        l2.append(t)
    else:
        l3.append(t)
    t += 1

l = l2 + l3
print(l[k-1])
 """
n, k = map(int, input().split())
print((k - (n + 1) // 2) * 2 if k > (n + 1) // 2 else k * 2 - 1)