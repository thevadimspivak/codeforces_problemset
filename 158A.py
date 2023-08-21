n, k = map(int, input().split())
s = list(map(int, (input().split())))
min = s[k-1]
t = 0

if sum(s) == 0:
    print(0)
else:
    if min == 0:
        for i in s:
            if i > min:
                t += 1
        print(t)
    else:
        for i in s:
            if i >= min:
                t += 1
        print(t)  
      



