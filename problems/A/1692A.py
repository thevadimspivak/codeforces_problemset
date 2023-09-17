n = int(input())

for i in range(n):
    x = input().split()
    a = x.pop(0)
    x = map(int, x)
    count = 0
    for j in x:
        if j > int(a):
            count += 1

    print(count)