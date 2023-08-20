l = input()
c = 0
c2 = 0
for letter in l:
    if letter == '0' and c < 7 and c2 < 7:
        c += 1
        c2 = 0
    elif letter == '1' and c < 7 and c2 < 7:
        c2 += 1
        c = 0
    elif c >= 7 or c2 >= 7:
        break
    else:
        c = 0
if c >= 7 or c2 >= 7:
    print('YES')
else:
    print('NO')