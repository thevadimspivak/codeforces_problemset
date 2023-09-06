n = int(input())


for i in range(n):
    t = int(input())
    s = list(map(int, input().split()))
    s = sorted(s)
    if len(s) == 1:
        print('YES')
    else:
        for ind in range(t - 1):
            if abs(s[ind] - s[ind+1]) > 1:
                print('NO')
                break
            else:
                t -= 1

            if t == 1:
                print('YES')



                