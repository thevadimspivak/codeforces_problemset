s = list(input())
hello_word = 'hello'
hello_word = list(hello_word)
count = 0
for letter in hello_word:
    for ind, elem in enumerate(s):
        if letter == elem:
            s = s[ind+1:]
            count += 1
            break

if count == 5:
    print('YES')
else:
    print('NO')