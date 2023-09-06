n, k = map(int, input().split())

t_min = 240
sum = 0
count = 0

for i in range(1, n + 1):
    t_on_contest = 5 * i
    sum += t_on_contest
    
    if k + sum > t_min:
        break
    else:
        count += 1
    
print(count)