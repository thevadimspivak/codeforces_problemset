n, m = map(int, input().split())
# n, m = [int(i) for i in input().split()] Идентичная запись
l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

index_n = l.index(n)

if index_n == len(l) - 1:
    print('NO')
else:
    if l[index_n + 1] == m:
        print('YES')
    else:
        print('NO')


""" i = 2
t = 0
while i < m:
    if m % i == 0:
        t += 1
    i += 1

if t > 0:
    print('NO')
else:
    print('YES') """