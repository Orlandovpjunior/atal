# goodString
def resolver(s, l, r, c):

    tamanho = r - l

    if tamanho == 1:
        if s[l] == c:
            return 0
        else:
            return 1

    meio = l + tamanho // 2

    custo1 = 0
    for i in range(l, meio):
        if s[i] != c:
            custo1 += 1
    custo1 += resolver(s, meio, r, chr(ord(c) + 1))

    custo2 = 0
    for i in range(meio, r):
        if s[i] != c:
            custo2 += 1
    custo2 += resolver(s, l, meio, chr(ord(c) + 1))

    return min(custo1, custo2)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    resultado = resolver(s, 0, n, 'a')
    print(resultado)