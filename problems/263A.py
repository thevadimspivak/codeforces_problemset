m = []

for i in range(5):
    x = input().split()
    x = list(map(int, x))
    m.append(x)

for i in range(5):
    for j in range(5):
        if m[i][j] == 1:
            t = abs(i - 2) + abs(j - 2)
            break

print(t)