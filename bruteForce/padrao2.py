a1 = 'farda'
b1 = 'fardamento'

a2 = 'fardamento'
b2 = 'farda'

a3 = 'feliz'
b3 = 'felicidade'

def StringMatcher(a: str, b: str) -> bool:

    n = len(b)
    m = len(a)
    
    if m > n: return False
    for i in range(n - m + 1):
        j = 0
        while j < m and a[j] == b[i + j]:
            j += 1
        if j == m: return True
    return False

print(f"'{a1}' aparece em '{b1}'? {StringMatcher(a1, b1)}")
print(f"'{a2}' aparece em '{b2}'? {StringMatcher(a2, b2)}")
print(f"'{a3}' aparece em '{b3}'? {StringMatcher(a3, b3)}")