n = int(input())
gifts = list(map(int, input().split()))

for i in range(n):
    print(gifts.index(i + 1) + 1, end=' ')
