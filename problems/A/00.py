n = int(input())
s = list(map(int, input().split()))

m = max(s)
total = 0 

for i in s:
    x = m - i
    total += x

print(total)