n, t = map(int, (input().split()))
q = list(map(str, input()))


j = 1
while j <= t:
    i = 0
    while i < n - 1: 
        if q[i] == 'B' and q[i + 1] == 'G':
            q[i] = 'G'
            q[i +1] = 'B'
            i += 1
        i += 1
        
    j += 1
    


print(''.join(q))