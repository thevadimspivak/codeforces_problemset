
n = int(input().split()[0])

words = []

for word in range(n):
    words.append(input())


for word in words:
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word) 