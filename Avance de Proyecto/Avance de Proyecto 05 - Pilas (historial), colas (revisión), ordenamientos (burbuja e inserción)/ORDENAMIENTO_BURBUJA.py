# implementacion del ordenamiento de burbuja para el proyecto 

def ordenamiento_burbuja(lista):
    n = len(lista)
    # se recorre la lista multiples veces
    for i in range(n):
        # en cada pasad se compara cada par de elementos adyacentes
        for j in range(0, n - i - 1):
            # si un elemento es mayor que el siguiente se intercambian
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


