men = input() + input()
mixed = input()

if len(men) != len(mixed):
    print('NO')
    exit()
else:
    for c in men:
        if men.count(c) != mixed.count(c):
            print('NO')
            exit()
print('YES')