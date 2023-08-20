n = [int(i) for i in input()]

t = 0

for j in range(len(n)):
    if n[j] == 4 or n[j] == 7: t += 1   
    else: 
        t *= 0
        break

if t > 0 or len(n) == 7 or len(n) == 4:
    print('YES')
else:
    print('NO')

