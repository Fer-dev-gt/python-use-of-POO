"""Con este algoritmo (de O(n log n))vamos dividiendo listas constantemente hasta que solo tengan 1 valor cada una (usando Recursividad) y luego las comparamos y ordenamos. Vamos de listas largas a listas cortas y luego las vamos ordenando desde las listas cortas hasta las lista largas. Recuerda: Divide y Conquista"""

import random

def ordenamiento_por_mezcla(lista):
    """Esta parte de la función tiene complejidad algoritmica de 'O(log n)'"""
    if len(lista) > 1:                                          # Si la lista es de 1 elemento entonces por definicion ya esta ordenada
        medio = len(lista) // 2                                 # Dividimos la lista a la mitad con "Floor Division"
        # Aplicamos "slicing", creamos 2 listas
        izquierda = lista[:medio]                               # Dividimos una lista a la mitad (valor de "medio"), es el lado izquierdo
        derecha = lista[medio:]                                 # Hacemos otra lista pero que comienza del valor de "medio"
        print(izquierda, '*' * 5, derecha)                      # Imprimimos los valores de las 2 listas, (se imprime varias veces)

        # Aplicamos recursividad en cada mitad, se ejecutan hasta que solo quedan lista de solo 1 valor
        ordenamiento_por_mezcla(izquierda)                      # Mandamos lista "izquierda" como parametro a la funcion con recursividad y se ejecuta
        ordenamiento_por_mezcla(derecha)                        # Mandamos lista "derecha" como parametro a la funcion con recursividad y se ejecuta

        # Iteradores para recorrer las 2 sublistas
        i = 0   # lista "izquierda"                             # Esto servirá bastante cuando las listas sean mas largas para compararlo con el valor de la lista del otro lados
        j = 0   # lista "derecha"                               # Esto servirá bastante cuando las listas sean mas largas para compararlo con el valor de la lista del otro lados
        # Iterador para la lista principal
        k = 0   # lista "lista", sera el indice de la lista principal

        """Esta parte de la función tiene complejidad algoritmica de 'O(n)'"""
        # Ciclo para comparar el valor de la izquierda con el de la derecha
        while i < len(izquierda) and j < len(derecha):          # Esto nos asegura que podamos hacer comparacion entre las listas
            if izquierda[i] < derecha[j]:                       # Comparamos cual valor de lista es mayor
                lista[k] = izquierda[i]                         # El valor de la izquierda es menor al de la derecha, la agregamos a lista principal
                i += 1
            else: 
                lista[k] = derecha[j]                           # Paso el valor de la derecha a la izquierda porque es menor al valor de la derecha
                j += 1                                          

            k += 1                                              # Aumentas "k", que seria el del indice de la lista principal
        
        # Solo uno de los dos siguentes ciclos se cumplira
        # Ciclo para
        while i < len(izquierda):
            lista[k] = izquierda[i]                             # Guardamos el valor mayor a la siguiente posición (atras aplicamos "k += 1") ahora "k" vale una posicion más
            i += 1
            k += 1                                              # Independientemente del resultado "k" siempre aumentara su valor por 1

        while j < len(derecha):                                 # Guardamos el valor mayor a la siguiente posición (atras aplicamos "k += 1") ahora "k" vale una posicion más
            lista[k] = derecha[j]
            j += 1      
            k += 1                                              # Independientemente del resultado "k" siempre aumentara su valor por 1

        print(f'izquierda {izquierda}, derecha {derecha}')          # Imprimimos la lista de "izquierda" y la de "derecha"
        print(f'Porción de lista ordenada: \n{lista}')            
        print('-' * 35)

    return lista


if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño sera la lista? '))    

    lista = [random.randint(0, 9) for i in range(list_size)]
    print(f'Lista desordenada: \n{lista}  \n{"-" * 35}')

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(f'Lista ordenada: \n{lista_ordenada}')
    