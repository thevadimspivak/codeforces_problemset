n = int(input())
count1 = 0
count2 = 0


for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        count1 += 1
    elif b > a:
        count2 += 1

if count1 > count2:
    print('Mishka')
elif count2 > count1:
    print('Chris')
else:
    print('Friendship is magic!^^')
