s = input()

up = 0
low = 0

for i in s:
    if (i.isupper()):
        up += 1
    else: low += 1

if up > low: print(s.upper())
if up <= low: print(s.lower())    
    
   

    
    
    
    
    
