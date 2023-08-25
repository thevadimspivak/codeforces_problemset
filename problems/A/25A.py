n = int(input())
s = list(map(int, input().split()))
chet = 0
nechet = 0
i = 0
while i < n:
    if s[i] % 2 == 0:
        chet += 1
    else:
        nechet += 1
    i += 1



if chet > nechet:
    for j in s:
        if j % 2 != 0:
            print(s.index(j) + 1)
        
else:
    for j in s:
        if j % 2 == 0:
            print(s.index(j) + 1)
        