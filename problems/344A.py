n = int(input())
count = 1
magnets = []
for i in range(0, n):
    m = input()
    magnets.append(m)
for i in range(0, n-1):
    if (magnets[i]) != (magnets[i+1]): count += 1

     
print(count)