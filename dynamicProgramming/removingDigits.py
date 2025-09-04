# removingDigits

n = int(input())
dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for digit_char in str(i):
        digit = int(digit_char)
        if digit != 0:
            dp[i] = min(dp[i], dp[i - digit] + 1)

print(dp[n])