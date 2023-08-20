n = input()[1:][:-1]

m = dict.fromkeys(n.split(', '))

if len(m) == 1:
    print('0')
else:
    print(len(m))

