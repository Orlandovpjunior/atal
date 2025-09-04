# thewaytohome

n, d = map(int, input().split())
s = input()

dp = [float('inf')] * (n + 1)
dp[1] = 0

for i in range(1, n + 1):
    
    if s[i-1] == '1':
        for j in range(1, d + 1):
            
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + 1)

print(-1) if dp[n] == float('inf') else print(dp[n])