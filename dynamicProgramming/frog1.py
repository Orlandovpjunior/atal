# frog1

n = int(input())
pedras = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0

for i in range(1, n):
    dp[i] = min(dp[i], dp[i - 1] + abs(pedras[i] - pedras[i - 1]))
    if i > 1:
        dp[i] = min(dp[i], dp[i - 2] + abs(pedras[i] - pedras[i - 2]))

print(dp[-1])