from bokeh.models import ColumnDataSource                                                           # Importamos diferentes modulos, librerias y funciones
from bokeh.palettes import Bright6
from bokeh.plotting import figure, show, output_file
from bokeh.transform import factor_cmap

if __name__ == '__main__':
    output_file('goles_anotados.html')                                                              # Nombramos el documento output (html)
    numero_jornada = ['Jornada 1', 'Jornada 2', 'Jornada 3', 'Jornada 4', 'Jornada 5',]             # Eje "x"
    goles_anotados = [2, 1, 1, 3, 4]                                                                # Eje "y"

    diccionario = ColumnDataSource(data=dict(numero_jornada=numero_jornada, goles_anotados=goles_anotados))  # Unificamos los datos en un diccionario

    grafica = figure(x_range=numero_jornada, height=350, toolbar_location=None, title="Goles anotados por jornada de Platzi FC")        # Generamos la grafica
                                                                                                                                        # Le agregamos los datos fuente y caracteristicas de como va a mostrar la grafica
    grafica.vbar(x='numero_jornada', top='goles_anotados', width=0.9, source=diccionario, legend_field="numero_jornada", line_color='white', fill_color=factor_cmap('numero_jornada', palette=Bright6, factors=numero_jornada))

    # Personalizamos el aspecto de la gráfica
    grafica.xgrid.grid_line_color = None
    grafica.y_range.start = 0
    grafica.y_range.end = 5
    grafica.legend.orientation = "horizontal"
    grafica.legend.location = "top_center"

show(grafica)                                               # Mostramos la gráfica