n = [int(i) for i in input()]
m = [int(i) for i in input()]
s = []
for i in range(len(n)):
    if n[i] != m[i]:
        s.append('1')
    else:
        s.append('0')

print(''.join(s))

