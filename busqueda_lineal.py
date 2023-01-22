"""Para tener una buena estimacion de lo que va a tardar hay que 'SIEMPRE PENSAR EN EL PEOR DE LOS CASOS'
Total de compejidad algoritmoca: O(n) + O(n) = O(n + n) = O(2n) = O(n) es una función lineal"""

import random

def busqueda_lineal(list, objective):
    encontrado = False                                              # False ya que al iniciar la funcion "busqueda_lineal" aun no hemos encontrado el "objective"
    pasos_tomados = 0

    for element in list:                                            # Complejidad algoritmica = O(n), recorremos la lista
        pasos_tomados += 1                                          # Contamos cuantas veces busco en la lista

        if element == objective:                                    # Si el elemento esto en la lista le cambiamo el valor de "encontrado" a True                         
            encontrado = True
            break                                                   # Salimos del ciclo usando "break"

    return encontrado, pasos_tomados                                # Regresamos 2 valores, si "element" no esta en la lista, regresamos False


if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño sera la lista? '))
    objective = int(input('¿Qué número quieres encontrar? '))
    lista = [random.randint(0, 100) for i in range(list_size)]                          # Llenamos la lista de números aleatoreos, estan desordenados

    encontrado, pasos_tomados = busqueda_lineal(lista, objective)                       # Ejecutamos funcion busqueda_lineal, devuelve 2 valores, "encontrodo" = "encontrado"

    print(f'Lista desordenada: \n{lista}')
    print(f'El número {objective} {"esta" if encontrado else "no esta"} en la lista')   # Para poner una condicion al print utilizamos "operadores ternarios"
    print(f'El número de pasos que realizó el algoritmo fueron: {pasos_tomados}')       # Mostramos cuantos pasos hizo la función
