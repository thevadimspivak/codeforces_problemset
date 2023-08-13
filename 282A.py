n = int(input())
x = 0

for i in range(0, n):
    t = input()
    if t.count('++'):
        x += 1
    elif t.count('--'):
        x -= 1

print(x)