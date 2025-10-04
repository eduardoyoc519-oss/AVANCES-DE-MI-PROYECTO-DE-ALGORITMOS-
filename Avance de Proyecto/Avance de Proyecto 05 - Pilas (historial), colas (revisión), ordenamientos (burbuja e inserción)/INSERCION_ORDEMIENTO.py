# implementacion del ordenamiento por insercion 
#este al igual que el de burbuja nos puede ayuar para el orden del proyecto 

def ordenamiento_insercion(lista):
    # se recorre la lista desde el segundo elemento
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i

        # se desplazan los elementos mayores que el valor actual
        # hacia la derecha para hacer espacio
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion = posicion - 1
        
        # se inserta el valor actual en su posicion correcta
        lista[posicion] = valor_actual
    return lista




