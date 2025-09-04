# permutationTransformation

def calcular_profundidades(array, inicio, fim, profundidade, mapa_de_profundidades):
    if inicio > fim:
        return

    indice_max = inicio
    for i in range(inicio + 1, fim + 1):
        if array[i] > array[indice_max]:
            indice_max = i
    
    valor_no = array[indice_max]
    mapa_de_profundidades[valor_no] = profundidade

    calcular_profundidades(array, inicio, indice_max - 1, profundidade + 1, mapa_de_profundidades)

    calcular_profundidades(array, indice_max + 1, fim, profundidade + 1, mapa_de_profundidades)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    profundidades = {}
    calcular_profundidades(a, 0, n - 1, 0, profundidades)

    resultado_final = []
    for valor in a:
        resultado_final.append(str(profundidades[valor]))
    
    print(" ".join(resultado_final))