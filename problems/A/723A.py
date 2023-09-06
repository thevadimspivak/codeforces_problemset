from math import ceil

n = list(map(int, input().split()))

max_n = max(n)
min_n = min(n)

for i in n:
    if i != min_n and i != max_n:
        centr = i

print(max_n - centr + centr - min_n)