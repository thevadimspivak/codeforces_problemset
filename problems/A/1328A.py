n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a % b != 0:
        c = a // b + 1
        d = b * c - a
        print(d)
    else:
        print(0)