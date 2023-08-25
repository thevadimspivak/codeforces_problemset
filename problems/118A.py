s = input()
al = ['a', 'o', 'y', 'e', 'u', 'i']
s = s.lower()
l = []

for i in s:
    if i not in al:
        l.append(i)

w = '.'.join(l)
print('.' + w)    
    