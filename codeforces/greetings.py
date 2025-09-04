# greetings

def merge_sort_e_contar_inversoes(arr):
    if len(arr) <= 1:
        return arr, 0
    
    meio = len(arr) // 2
    
    metade_esquerda, inv_esquerda = merge_sort_e_contar_inversoes(arr[:meio])
    metade_direita, inv_direita = merge_sort_e_contar_inversoes(arr[meio:])
    
    arr_mesclado, inv_cruzadas = merge_e_contar(metade_esquerda, metade_direita)
    
    total_inversoes = inv_esquerda + inv_direita + inv_cruzadas
    return arr_mesclado, total_inversoes

def merge_e_contar(esquerda, direita):
    resultado = []
    inversoes = 0
    i = 0 
    j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            inversoes += len(esquerda) - i
            j += 1
            
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado, inversoes

t = int(input())
for _ in range(t):
    n = int(input())
    pessoas = []
    for i in range(n):
        a, b = map(int, input().split())
        pessoas.append((a, b))
    
    pessoas.sort()
    
    posicoes_finais = [p[1] for p in pessoas]
    
    _, total_de_saudacoes = merge_sort_e_contar_inversoes(posicoes_finais)
    
    print(total_de_saudacoes)