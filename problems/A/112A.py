l = []
for line in range(2):
    x = input()
    l.append(x.lower())

if l[0] < l[1]:
    print('-1')
elif l[0] > l[1]:
    print('1')
else:
    print('0')
    

