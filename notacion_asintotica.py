"""
IMPORTANTE, TODOS LOS ALGORITMO EXPONENCIALES, TIRALOS A LA BASURA CONSUMEN MUCHOS RECURSOS, AHORA LOS CUADRATRICOS TODAVIA PUEDEN SERVIR SI TIENEN POCOS INPUTS 
"""
# Ejemplo de ley de la suma
def f(n):

    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)

# Usando "Big O Notacion" se puede entender que: 
"""O(n) + O(n) = O(n + n) = O(2n) = O(n)"""    # Esto por que aqui no importan los terminos especificos
# Esa ecuacion reprenta el numero de operaciones del programa


# Ejemplo de ley de la suma con exponenciales
def f_2(n):

    for i in range(n):
        print(i)
    
    for i in range(n * n):  # Esto se convierte a "n^2"
        print(i) # Este va a ser el mas decisivo por la cantidad de operaciones y el que nos va a interesar
""" O(n) + O(n * n) = O(n + n^2) = O(n^2)"""


# Ejemplo de ley de la multiplicacion
def f_3(n):
    # Esto es una iteracion anidada
    for i in range(n):
        for j in range(n): 
            print(i, j)
""" O(n) * O(n) = O(n * n) = O(n^2)"""


# Ejemplo de Recursividad multiple
def fibonacci(n): # Cada vez que ejecutamos esta funcion fibonacci, estamos ejecutando otras 2 funciones fibonaccis
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
"""O(2^n)"""