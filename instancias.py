class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodo para calcular la distancia entre 2 coordenadas, una en "x" y la otra en "y"
    def distancia(self, otra_coordenada): 
        diferencia_en_x = (self.x - otra_coordenada.x) ** 2 # "otra_coordenada.x" significa valor en x del objeto enviado
        diferencia_en_y = (self.y - otra_coordenada.y) ** 2

        return (diferencia_en_x + diferencia_en_y) ** 0.5 # Calculamos raiz cuadrada elevando la suma a la 0.5 potencia
    

if __name__ == '__main__':
    # Aqui generamos una "instancia/objeto" y mandamos los valores que tendran sus atributos
    coordenada_1 = Coordenada(3, 30) 
    coordenada_2 = Coordenada(4, 8) # En total creamos 2 Objetos


    """Aqui imprimimos la distancia entre 2 coordenadas (Los dos objetos que creamos) y usamos el "Método" de la "Clase Coordenada", este método mide la distancia de dos puntos"""

    print(coordenada_1.distancia(coordenada_2)) # Es este caso, primero va el objeto de referencia, luego ejecutamos el método e pasamos como parametro el otro objeto "coordenada_2"

    # Este es un método especial que nos dice si un objeto es instancia de la clase indicada
    print(f'coordenada_2 si es una instancia de clase Persona, {isinstance(coordenada_2, Coordenada)}')
    print(f'3 no es una instancia de clase Persona, {isinstance(3, Coordenada)}') # En este caso es False ya que nunca declaramos "3" como instancia de "Coordenada"
