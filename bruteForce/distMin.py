from math import sqrt

pontos = [(1, 1), (2, 1), (3, 2), (4, 1)]

def distMin(pontos: list) -> tuple[int, int, float]:
    
    n = len(pontos)
    dist = float('INF')
    
    for i in range(n):
        for j in range(i + 1, n):
            x1,y1 = pontos[i]
            x2,y2 = pontos[j]
            
            d = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            
            if d < dist:
                dist = d
                index1 = i
                index2 = j
    
    return index1, index2
            
print(distMin(pontos))
            
            
            