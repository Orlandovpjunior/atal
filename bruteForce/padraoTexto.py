texto = 'abcabaabcabac'
padrao = 'abaa'

def stringMatcher(t: str, p: str) -> None:
    
    n = len(t)
    m = len(p)
    
    for i in range(n-m):
        j = 0
        
        while j < m and padrao[j] == t[i + j]:
            j += 1
        if j == m: print("O padrao ocorre com descolamento ", i)

stringMatcher(texto,padrao)
