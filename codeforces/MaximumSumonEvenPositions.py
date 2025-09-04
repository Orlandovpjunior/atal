# MaximumSumonEvenPositions

def kadane(arr):
    max_ate_agora = 0
    max_atual = 0
    for x in arr:
        max_atual += x
        if max_atual < 0:
            max_atual = 0
        max_ate_agora = max(max_ate_agora, max_atual)
    return max_ate_agora

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    soma_base = 0
    for i in range(0, n, 2):
        soma_base += a[i]
    diffs1 = []
    for i in range(0, n - 1, 2):
        diffs1.append(a[i+1] - a[i])

    diffs2 = []
    for i in range(1, n - 1, 2):
        diffs2.append(a[i] - a[i+1])
        
    ganho_maximo = 0
    if diffs1:
        ganho_maximo = max(ganho_maximo, kadane(diffs1))
    if diffs2:
        ganho_maximo = max(ganho_maximo, kadane(diffs2))

    print(soma_base + ganho_maximo)