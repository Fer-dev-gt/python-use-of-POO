import random

# Funcion que aplica el "Ordenamiento de Burbuja"
def ordenamiento_de_burbujas(lista):
    list_length = len(lista)

    for i in range(list_length):
        for j in range(0, list_length - i - 1):                               # Posicion final: Tamaño de lista - lo que ya recorrimos - 1 (index, off by one)
            #print(i, j)                                            # para ver ciclos anidados
            if lista[j] > lista [j + 1]:                            # Comparamos lugar en "j" con su valor a la derecha "j + 1"
                lista[j], lista[j + 1] = lista[j + 1], lista[j]     # Realizo el intercambio "Swaping" (valor e index)
                print(lista)                                        # Para ver como se desarrolla el algoritmo paso a paso
    return lista


if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño sera la lista? '))    

    lista = [random.randint(0, 9) for i in range(list_size)] # Llenamos la lista con numeros aleatoreos
    print(f'Lista desordenada: \n{lista}  \n{"-" * 25}')

    lista_ordenada = ordenamiento_de_burbujas(lista)
    print(f'{"-" * 25}\nLista ordenada: \n{lista_ordenada}')
    

"""Complejidad algoritmica:
O(n) * O(n - i - 1) = O(n) * O(n) = O(n * n) = O(n^2)
"""