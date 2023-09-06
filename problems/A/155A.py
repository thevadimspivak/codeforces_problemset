n = input()
s = list(map(int, input().split()))
new_s = []
count = 0

first_elem = s.pop(0)
new_s.append(first_elem)

while s:
    if s[0] > max(new_s):
        count += 1
        new_s.append(s.pop(0))
    elif s[0] < min(new_s):
        count += 1
        new_s.append(s.pop(0))
    else:
        new_s.append(s.pop(0))


print(count)