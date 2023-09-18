# t = int(input())

# for i in range(t):
#     x, y, n = map(int, input().split())
#     for k in range(n, -1, -1):
#         if k % x == y:
#             print(k)
#             break
t = int(input())

for _ in range(t):
    x, y, n = map(int, input().split())
    
    # Вычисляем остаток от деления y на x
    remainder = y % x
    
    # Вычисляем максимальное k, удовлетворяющее условиям
    if remainder <= n % x:
        k = n - (n % x) + remainder
    else:
        k = n - (n % x) - (x - remainder)
    
    print(k)