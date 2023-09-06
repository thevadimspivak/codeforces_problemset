
n = int(input())
s = list(map(int, input().split()))

player_1 = 0
player_2 = 0
move = 0

while s:
    move += 1
    if s[0] > s[-1]:
        if move % 2 != 0:
            player_1 += s.pop(0)
            
        else:
            player_2 += s.pop(0)
    else:
        if move % 2 != 0:
            player_1 += s.pop(-1)
        else:
            player_2 += s.pop(-1)

print(player_1, player_2)