# equivalentStrings

def canonical(string):

    n = len(string)

    if n % 2 == 1:
        return string

    meio = n // 2
    s1_str = string[:meio]
    s2_str = string[meio:]


    s1_canonical = canonical(s1_str)
    s2_canonical = canonical(s2_str)

    if s1_canonical < s2_canonical:
        return s1_canonical + s2_canonical
    else:
        return s2_canonical + s1_canonical

a = input()
b = input()

if canonical(a) == canonical(b):
    print("YES")
else:
    print("NO")