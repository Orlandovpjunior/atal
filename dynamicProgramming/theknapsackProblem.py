s, n = map(int, input().split())

valores = []

for _ in range(n):
    peso, valor = map(int, input().split())
    valores.append((peso,valor))

dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]

for i in range(1 , n + 1):
    peso_atual, valor_atual = valores[i - 1]
    
    for j in range(1, s + 1):
        dp[i][j] = dp[i - 1][j]
        
        if peso_atual <= j:
            dp[i][j] = max(dp[i - 1][j], valor_atual + dp[i - 1][j - peso_atual])
print(dp[n][s])