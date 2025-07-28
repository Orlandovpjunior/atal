a, b = map(int, input().split())

def backtrack(valor, alvo, caminho):
    if valor == alvo:
        print("YES")
        print(len(caminho))
        print(' '.join(map(str, caminho)))
        return True
    if valor > alvo:
        return False
    if backtrack(valor * 2, alvo, caminho + [valor * 2]):
        return True
    if backtrack(valor * 10 + 1, alvo, caminho + [valor * 10 + 1]):
        return True
    return False

if not backtrack(a, b, [a]):
    print("NO")