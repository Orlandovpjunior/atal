b = [1, 2, 5, 6, 8]
alvo = 9

def backtrack(lista,indice, soma_parcial, resultado, solucoes):
    if indice == len(lista):
        if soma_parcial == alvo:
            solucao = []
            for i in range(len(lista)):
                if resultado[i] == 1:
                    solucao.append(lista[i])
            solucoes.append(solucao)
        return
    
    resultado[indice] = 1
    backtrack(lista, indice + 1, soma_parcial + lista[indice], resultado, solucoes)
    
    resultado[indice] = 0
    backtrack(lista, indice + 1, soma_parcial, resultado, solucoes)

resultado = [0] * len(b)
solucoes = []

backtrack(b,0, 0, resultado, solucoes)

print("Soluções encontradas:")
for sol in solucoes:
    print(sol)
        
        
    