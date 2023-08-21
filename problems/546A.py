k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)

t = 1
s = 0

while t <= w:
    tt = k * t
    t += 1
    s += tt

if n >= s:
    print('0')
else:
    print(abs(n-s))

    