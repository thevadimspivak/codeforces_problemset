n = int(input())
l = list(map(int, input().split()))

count = 1
max_good = 1
for i in range(n-1):
    if l[i] <= l[i+1]:
        count +=1
        if count >= max_good:
            max_good = count
        
    else:
        count = 1

print(max_good)