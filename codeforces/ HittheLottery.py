#  HittheLottery

n = int(input())

coins = [100,20,10,5,1]
count = 0

for c in coins:
    count += n // c
    n = n % c
    
print(count)