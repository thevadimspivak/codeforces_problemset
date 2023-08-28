n = int(input())
s = list(map(int, input().split()))

percent = sum(s)/len(s)
print('{:.9f}'.format(percent))

