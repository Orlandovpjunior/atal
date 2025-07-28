from collections import deque

a, b = map(int,input().split())

lista = [a]
pre = {}
fila = deque([a])

while fila:
    v = fila.popleft()
    
    if v * 2 not in pre and v * 2 <= b:
        fila.append(v * 2)
        pre[v * 2] = v
    if v * 10 + 1 not in pre and v * 10 + 1 <= b:
        fila.append(v * 10 + 1)
        pre[v * 10 + 1] = v

seq = [b]

if b not in pre:
    print("NO")
else:
    print("YES")
    x = b
    while x != a:
        x = pre[x]
        seq.append(x)
    print(len(seq))
    
    seq.reverse()
    for i in seq:
        print(i)