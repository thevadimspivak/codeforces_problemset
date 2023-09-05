n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)
total_sum = sum(coins)
current_sum = 0
coins_taken = 0

for coin in coins:
    current_sum += coin
    coins_taken += 1
    if current_sum > total_sum / 2:
        break

print(coins_taken)