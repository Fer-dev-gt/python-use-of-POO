"""Creamos una ecuacion que represente el numero de operacion que realizara este código, total de operacion = 1002 + x + 2x^2"""

def conteo_abstracto(x):                                       # 2(x * x) = 2x^2
    response = 0                                # Cuenta como 1 operacion

    for i in range(1000):                       # Va a iterar 1000 veces y cuenta como 1000 operaciones
        response += 1

    for i in range(x):                          # El numero de iteraciones depende de "x", seran un "x" numero de operaciones
        response += 1  

    for i in range(x):
        for j in range(x):  
            response += 1
            response += 1                       
            print(i, j)

    return response                             # Cuenta como 1 operacion

prueba = conteo_abstracto(10)
print(f'Pasos que realizó el programa: \n{prueba}')