a, b = list(map(int, input().split()))

count = 1

while a:
    temp = a * count
    if temp % 10 == 0 or temp % 10 == b:
        print(count)
        break
    else:
        count += 1