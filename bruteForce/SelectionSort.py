arr = [3, 2, 4, 1, 5]

def swap(arr: list, i: int, j: int) -> None:
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux

def selectionSort(arr: list) -> list:
    n = len(arr)
    
    for i in range(n):
        indice_menor = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[indice_menor]:
                indice_menor = j
        
        swap(arr, i, indice_menor)
    
    return arr

resultado = selectionSort(arr)
print("Array ordenado:", resultado)
        

