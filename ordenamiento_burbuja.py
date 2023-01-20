import random

# Funcion que aplica el "Ordenamiento de Burbuja"
def ordenamiento_de_burbujas(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # Posicion final: Tamaño de lista - lo que ya recorrimo - 1 (index)
            #print(i, j) #para ver for anidados
            if lista[j] > lista [j + 1]: # Comparamos segun los valores y su posicion en la lista
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # Realizo el intercambio "Swaping"
                print(lista) # Para ver como se desarrolla el algoritmo paso a paso
    return lista


if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño sera la lista? '))    

    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbujas(lista)
    print(lista_ordenada)
    

"""Complejidad algoritmica:
O(n) * O(n - i - 1) = O(n) * O(n) = O(n * n) = O(n^2)
"""