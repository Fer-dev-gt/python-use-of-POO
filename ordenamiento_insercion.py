import random 
# Conceptualmente usamos 2 listas, pero en el codigo trabajamos solo con una lista
# Este es un algmoritmo de O(n^2)
def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]                                                                    # El primer valor de la lista desordenada
        posicion_actual = indice                                                                        # Lo usaremos para comparar los valores ubicados en los indices que hace referencia

        # Se cumplen las 2 condiciones, cuando "posicion_actual" es 0 llegamos al inicio de la lista
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:                        # Si el valor de la lista ordenada es mayor al primer valor de la lista desordenada
            lista[posicion_actual] = lista[posicion_actual - 1]                                         # Paso el valor a la derecha, hacemo "Swaping"
            posicion_actual -= 1                                                                        # Corremos el indice a la izquierda, vamos para atras
            
        lista[posicion_actual] = valor_actual                                                           # Guardamos el valor en el indice que nos dio "posicion_actual" segun las comparaciones
        print(lista)                                                                                    # Para ver como se desarrolla el algoritmo paso a paso

    return lista
        

if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño sera la lista? '))    

    lista = [random.randint(0, 9) for i in range(list_size)] # Llenamos la lista con numeros aleatoreos
    print(f'Lista desordenada: \n{lista}  \n{"-" * 25}')

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(f'{"-" * 25}\nLista ordenada: \n{lista_ordenada}')
    