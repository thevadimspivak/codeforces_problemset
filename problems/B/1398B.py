t = int(input())

for i in range(t):
    s = list(input())
    move = 0
    alice = 0
    while s.count('1') != 0:
        max_count_of_1s = 0
        temp_max = 0
        for j in s:
            if j == '1':
                temp_max += 1
                if temp_max > max_count_of_1s:
                    max_count_of_1s = temp_max
            else:
                temp_max = 0        
        to_remove = max_count_of_1s * '1'
        new_s = ''.join(s)
        s = new_s.replace(to_remove, '', 1)
        move += 1     
        if move % 2 != 0:
            alice += max_count_of_1s
            
    print(alice)