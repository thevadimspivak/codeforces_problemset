m = []

for i in range(5):
    x = input().split()
    x = list(map(int, x))
    for j in x:
        m.append(j)

one = m.index(1)
print(13 - (one+1))