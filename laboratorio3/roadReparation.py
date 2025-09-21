import heapq

n, m = map(int,input().split())

grafo = {i: {} for i in range(1, n + 1)}

for _ in range(m):
    a,b,c = map(int, input().split())
    grafo[a][b] = c
    grafo[b][a] = c

fila = [(0,1)]
heapq.heapify(fila)

visitados = set()
custo_total = 0

while fila and len(visitados) < n:
    custo_atual, node_atual = heapq.heappop(fila)
    
    if node_atual in visitados:
        continue
    
    visitados.add(node_atual)
    custo_total += custo_atual
    
    for node, custo in grafo[node_atual].items():
        if node not in visitados:
            heapq.heappush(fila, (custo, node))
        
if len(visitados) == n:
    print(custo_total)
else:
    print("IMPOSSIBLE")