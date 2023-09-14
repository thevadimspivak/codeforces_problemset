n, m = map(int, input().split())
f = list(map(int, input().split()))

f.sort()  # Сортируем пазлы по возрастанию

min_diff = float('inf')  # Инициализируем минимальную разницу

left = 0
right = n - 1

while right < m:
    diff = f[right] - f[left]  # Вычисляем текущую разницу
    min_diff = min(min_diff, diff)  # Обновляем минимальную разницу
    left += 1
    right += 1

print(min_diff)  # Выводим минимальную разницу