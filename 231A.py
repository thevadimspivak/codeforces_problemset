n = int(input())

t = 0
for i in range(0, n):
    x = input()
    if x.count('1') >= 2:
        t += 1
print(t)