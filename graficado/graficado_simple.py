"""Importamos 3 funciones, "figure" es la ventana donde vamos a graficar, "output_file" genera el nombre del archivo que sera nuestro output (html en este caso), "show" nos permite generar un servidor que se prende y muestra el archivo html directamente en el Browser"""
from bokeh.plotting import figure, output_file, show                        # La libreria funcionara cuando activemos nuestro "Ambiente Virtual"


    
if __name__ == '__main__':                                                  # Vamos a ejecutar las funciones importadas como si fueran nativas
    output_file('graficado_simple.html')                                    # Creamos el nombre del archivo
    fig = figure()                                                          # Generamos la figura, podemos usar la funcion type(fig) para ver tigo de figura y funcion help() para ver sus metodos disponibles
    total_values = int(input('¿Cuantos valores quieres graficar? \n'))
    
    x_values = list(range(total_values))                                    # Generamos lista con valores en "x"
    y_values = []                                                           # Lista vacia de valores "y" que dependen de "x"

    for x in x_values:
        value = int(input(f'Valor "y" para valor en "x": \n{x}'))           # Solicito valores "y" que dependeran de "x"
        y_values.append(value)                                              # Agrego valores a lista "y"

    fig.line(x_values, y_values, line_width = 2)                            # Ingresamos parametro a la grafica, cada figura tiene sus reglas para ingresar parametros
    show(fig)                                                               # Mostramos la figura

