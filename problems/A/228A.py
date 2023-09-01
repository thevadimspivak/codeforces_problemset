s = list(map(int, input().split()))
d = list(dict.fromkeys(s))

print(len(s) - len(d))