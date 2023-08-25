n = int(input())

hate = 'I hate'
love = 'I love'

result = ''

i = 0

while i < n:
    if i % 2 == 0:
        if i == 0:
            result += hate
        else:
            result += ' that ' + hate
    else:
        result += ' that ' + love

    i += 1

result += ' it'
print(result)