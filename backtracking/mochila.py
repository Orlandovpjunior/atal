itens = [
    {"item": 1, "peso": 15, "valor": 20},
    {"item": 2, "peso": 5, "valor": 30},
    {"item": 3, "peso": 10, "valor": 50},
    {"item": 4, "peso": 5, "valor": 10}
]
capacidade = 16
maior_valor = 0
melhor_combinacao = []

def mochila(lista, indice, valor, peso_max):
    global maior_valor, melhor_combinacao
    
    if indice == len(itens):
        if valor > maior_valor:
            maior_valor = valor
            melhor_combinacao = lista[:]
        return
    
    if itens[indice]["peso"] <= peso_max:
        lista[indice] = 1
        mochila(lista, indice + 1, valor + itens[indice]["valor"], peso_max - itens[indice]["peso"])
    
    lista[indice] = 0
    mochila(lista, indice + 1, valor, peso_max)

X = [0] * len(itens)
mochila(X, 0, 0, capacidade)

print(f"Combinação: {melhor_combinacao}")
print(f"Valor total: {maior_valor}")