n = input()
s = map(int, input().split())

num_of_cops = 0
num_of_crimes = 0

for i in s:
    if i > 0:
        num_of_cops += i
    elif i == -1 and num_of_cops > 0:
        num_of_cops -= 1
    elif i == -1 and num_of_cops == 0:
        num_of_crimes += 1


print(num_of_crimes) 