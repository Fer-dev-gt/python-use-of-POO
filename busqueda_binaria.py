# La "Busqueda Binaria" asume que la lista esta ordenada
"""Cuando trabajamos con indices que vienen de una funcion 'len()' siempre le restamos 1 para evitar el error logico 'Off By One'.
El profe para resolver el problema primero realiza el 'signature' y lo que llevara las funciones para luego escribir el cuerpo de la funcion
Complejidad algoritmica O(log n), muy eficiente, de las mejores que hay"""

import random

def busqueda_binaria(lista, comienzo, final, objective, pasos_tomados = 0):                 # Declaramos 5 parametros, recibimos 4 argumentos, "pasos_tomados" usa valor por defecto

    print(f'Buscando {objective} entre {lista[comienzo]} y lista {lista[final - 1]}')       # Mostramos por donde esta buscado entre las listas divididas
    pasos_tomados += 1                                                                      # Contamos las veces que tuvo que buscar

    # Se ejecuta si no encotramos el numero
    if comienzo > final:                                                                    # Signica que el algoritmo no lo encontro, porque se hizo cada vez mas chico y luego lo cruzo
        return False, pasos_tomados                                                         # Retornamos False y los pasos le tomo

    medio = (comienzo + final) // 2                                                         # Partimos las listas a la mitad usando "Floor Division"
    
    if lista[medio] == objective:                                                           # Ya encontro el objetivo
        return True, pasos_tomados
    elif lista[medio] < objective:                                                          # Nos vamos a la mitad derecha, el "objective" es mayor
        return busqueda_binaria(lista, medio + 1, final, objective, pasos_tomados)          # Invocamos de nuevo la funcion con otros valores de indices (Recursividad)
    else:                                                                                   # Nos vamos a la mitad izquierda, el "objective" es menor
        return busqueda_binaria(lista, comienzo, medio - 1, objective, pasos_tomados)       # Invocamos de nuevo la funcion con otros valores de indices (Recursividad)
    


if __name__ == '__main__':
    list_size = int(input('¿De qué tamaño sera la lista? '))
    objective = int(input('¿Qué número quieres encontrar? '))
    lista = sorted([random.randint(0, 100) for i in range(list_size)])                      # Para hacer "Busqueda Binaria" tenemos que ordenar la lista
    print(f'\nValores de lista ordenada: \n{lista}\n{"-" * 45} ')                           

    encontrado, pasos_tomados = busqueda_binaria(lista, 0, len(lista), objective)           # Enviamos 4 parametros, lista, "comienzo de lista", "final de lista" y numero a buscar. Recibimos 2 resultados
    print(f'El elemento {objective} {"esta" if encontrado else "no esta"} en la lista')     # Aplicamos una condicional "if/else"en el mensaje que va depender si la funcion retorno un True o False
    print(f'El número de pasos que le tomo al algoritmo fueron: {pasos_tomados}')           # Mostramos los pasos tomados