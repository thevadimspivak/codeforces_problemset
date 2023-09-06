s = list(map(int, input().split()))

s = sorted(s)
abc = s[-1]
print(abc - s[0], abc - s[1], abc - s[2])