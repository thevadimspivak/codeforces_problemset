n = int(input())

for i in range(n):
    l = []
    s = list((input()))
    for ind, i in enumerate(s):
        if i != 0:
            num = i + (len(s) - ind - 1)*'0'
            num = int(num)
            if num > 0:
                l.append(num)
    print(len(l))
    l = sorted(l, reverse=True)
    l = map(str, l)
    print(' '.join(l))
           