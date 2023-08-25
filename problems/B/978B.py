n = int(input())
s = list(input())

i = 0
t = 0

while i <= (len(s) - 3):
    if (s[i] == 'x') and (s[i + 1] == 'x') and (s[i + 2] == 'x'):
        del s[i + 2]
        t += 1
        i -= 1
        

    i += 1

print(t)