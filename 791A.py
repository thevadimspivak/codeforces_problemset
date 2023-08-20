a, b = input().split()
year = 0
a = int(a)
b = int(b)
while a <= b:
    a = a * 3
    b = b * 2
    year += 1

print(year)