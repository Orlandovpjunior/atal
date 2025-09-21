casos = int(input())

tree = {i:[] for i in range(1, casos + 1)}
raizes = []

for i in range(1, casos + 1):
    gerente = int(input())
    
    if gerente == -1:
        raizes.append(i)
    else:
        tree[gerente].append(i)

def dfs(inicio):
    if not tree[inicio]:
        return 1
    
    altura_max = 0    
    for vizinho in tree[inicio]:
        altura_filho = dfs(vizinho)
        if altura_filho > altura_max:
            altura_max = altura_filho
            
    return altura_max + 1
altura = 0

for r in raizes:
    
    altura_r = dfs(r)
    altura = max(altura, altura_r)
    
print(altura)