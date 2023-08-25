y = int(input())
y += 1
while y > 0:
    t = dict.fromkeys(str(y))
    if len(t) == 4:
        print(''.join(t))
        break
    y += 1

