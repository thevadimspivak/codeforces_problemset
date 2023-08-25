numbers = [int(i) for i in input().split()]

n = numbers[0]
k = numbers[1]

i = 0

while i < k:
    if str(n)[-1] != '0':
        n -= 1
    else:
        n = int(n / 10)
    i += 1

print(n)