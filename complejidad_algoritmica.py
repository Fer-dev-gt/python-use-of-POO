"""Vamos a realizar 2 implementacionos de factorial una 'iterativa' y otra 'recursiva'
La desventaja de estos métodos es que no podemos predecir cual sera más rápide y eficiente
Ejemplo la "Busqueda Binarea" es tiene complejidad de O(Log n)"""

import time                                                # Importamos modulo "time" para medir el tiempo de ejecucion

def factorial(n):                                          # Esta es la solución "iterativa"
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response


def factorial_r(n):                                        # Esta es la solucion "recursiva"
    if n == 1:
        return 1

    return n * factorial_r(n - 1)

   
if __name__ == '__main__':
    n = 200000
    # Medimos el tiempo que tarda en ejecutarse de forma "iterativa"
    comienzo = time.time()                                                              # Medimos el tiempo antes de ejecutar la funcion
    factorial(n)
    final = time.time()
    print(f'Tiempo que tomo en ejecutarse iterativamente: {final - comienzo} seg')      # Imprimimos el resultado de la operacion de tiempo para saber cuanto tardo

    # Medimos el tiempo que tarda en ejecutarse de forma "recursiva"
    comienzo = time.time()                                                              # Medimos el tiempo antes de ejecutar la funcion
    factorial(n)
    final = time.time()
    print(f'Tiempo que tomo en ejecutarse recursivamente: {final - comienzo} seg')      # Imprimimos el resultado de la operacion de tiempo para saber cuanto tardo   


"""NOTA DE RESULTADOS: al inicio la forma recursiva era más rapida por diferencia minima luego al aumentar 'n' significativamente, la forma iterativa tomo la ventaja
Ejemplo cuando n = 200000
Tiempo que tomo en ejecutarse: 19.087673902511597 seg
Tiempo que tomo en ejecutarse: 19.382639169692993 seg"""