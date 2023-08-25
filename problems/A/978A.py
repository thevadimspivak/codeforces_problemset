n = int(input())
l = [int(i) for i in input().split()]

l2 = []

j = n - 1

while j >= 0:
    if l[j] not in l2:
        l2.append(l[j])

    j -= 1

l2.reverse()
print(len(l2))
print(*l2)