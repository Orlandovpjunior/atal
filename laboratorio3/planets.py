import heapq

n, m = map(int,input().split())
grafo = {i:{} for i in range(1, n + 1)}
custos = {i: float("inf") for i in range(1, n + 1)}
custos[1] = 0
restricoes = {i:set() for i in range(1 , n + 1)}

for _ in range(m):
    a, b, c = map(int,input().split())
    grafo[a][b] = c
    grafo[b][a] = c

for i in range(1, n + 1):
    partes = input().split()
    
    k = int(partes[0])
    if k > 0:
        tempos = map(int, partes[1:])
        restricoes[i] = set(tempos)

fila = [(0, 1)]

while fila:
    custo_atual, no_atual = heapq.heappop(fila)
    if custo_atual > custos[no_atual]:
        continue
    tempo_de_partida = custo_atual
    
    while tempo_de_partida in restricoes[no_atual]:
        tempo_de_partida += 1

    for vizinho, custo_viagem in grafo[no_atual].items():
        novo_custo_chegada = tempo_de_partida + custo_viagem
        
        if novo_custo_chegada < custos[vizinho]:
            custos[vizinho] = novo_custo_chegada
            heapq.heappush(fila, (novo_custo_chegada, vizinho))

print(custos[n]) if custos[n] != float("inf") else print(-1)