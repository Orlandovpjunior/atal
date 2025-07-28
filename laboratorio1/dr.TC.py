t = int(input())

def contaUns(stringBinaria: str):
    contador = 0
    for i in stringBinaria:
        if i == '1':
            contador += 1
    return contador

def backtrack(stringOriginal: str, posicao: int, stringsGeradas: list):
    if posicao == len(stringOriginal):
        total = 0
        for string in stringsGeradas:
            total += contaUns(string)
        print(total)
        return
    
    novaString = stringOriginal[:posicao] + ('0' if stringOriginal[posicao] == '1' else '1') + stringOriginal[posicao+1:]
    backtrack(stringOriginal, posicao + 1, stringsGeradas + [novaString])

for _ in range(t):
    n = int(input())
    s = input()
    backtrack(s, 0, [])