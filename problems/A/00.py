t = int(input())


for i in range(t):
    s = int(input())
    l = []
    for j in range(1, 1700):
        if j % 3 == 0 or j % 10 == 3:
            continue
        else:
            l.append(j)

    for ind, elem in enumerate(l):
        if ind + 1 == s:
            print(elem)
            break
