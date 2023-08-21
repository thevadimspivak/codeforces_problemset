n = int(input())
count = 0
for i in range(0, n):
    p, q = input().split()
    if (int(q)-int(p)) >= 2: count +=1

print(count)