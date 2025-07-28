conjunto = [1,2,3]

def backtrack(lista: list, visidados: list, resultado: list, solucao: list, n: int) -> list:
    
    if n == len(lista):
        resultado.append(solucao[:])
        
    for i in lista:
        if i not in visidados:
            visidados.append(i)
            solucao.append(i)
            backtrack(lista,visidados,resultado,solucao, n+1)
            solucao.pop()
            visidados.pop()
    return resultado

print(backtrack(conjunto, [],[],[],0))