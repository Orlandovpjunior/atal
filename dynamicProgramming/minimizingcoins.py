n, x = map(int,input().split())
coins = list(map(int, input().split()))

dp = [float('inf')] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    
    for c in coins:
        
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)
            
print(dp[x])