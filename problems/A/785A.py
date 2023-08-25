n = int(input())
total = 0

for i in range(n):
    line = input()
    if line.count('Tetrahedron'):
        total += 4
    elif line.count('Cube'):
        total += 6
    elif line.count('Octahedron'):
        total += 8
    elif line.count('Dodecahedron'):
        total += 12
    elif line.count('Icosahedron'):
        total += 20

print(total)
