n = 4

def valido(tabuleiro, linha, coluna):
    for i in range(linha):
        if tabuleiro[i] == coluna:
            return False
        if abs(tabuleiro[i] - coluna) == abs(i - linha):
            return False
    return True

def n_rainhas(tabuleiro, linha, solucoes):
    if linha == n:
        solucoes.append(tabuleiro[:])
        return
    
    for coluna in range(n):
        if valido(tabuleiro, linha, coluna):
            tabuleiro[linha] = coluna
            n_rainhas(tabuleiro, linha + 1, solucoes)

tabuleiro = [-1] * n
solucoes = []

n_rainhas(tabuleiro, 0, solucoes)

print(f"Soluções para {n}-rainhas:")
for i, sol in enumerate(solucoes):
    print(f"Solução {i+1}: {sol}")
    
    for linha in range(n):
        for coluna in range(n):
            if sol[linha] == coluna:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print() 