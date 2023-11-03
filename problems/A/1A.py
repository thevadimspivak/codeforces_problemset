n, m, a = map(int, input().split())

# Находим количество секций по горизонтали и вертикали
sections_horizontal = (n + a - 1) // a
sections_vertical = (m + a - 1) // a

# Находим общее количество плит
total_tiles = sections_horizontal * sections_vertical

print(total_tiles)
print(total_tiles)
print(total_tiles)