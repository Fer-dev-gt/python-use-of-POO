# Ejemplo de "Polimorfismo" donde modificaremos el funcionamiento del metodo de la "Superclase" en la "Subclase"
class Persona:      # No lleva parametros ya que no recibe ninguna "Clase"

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Estoy caminando')



class Ciclista(Persona): # La clase Ciclista (Subclase) extienda a Persona (Superclase)
    
    def __init__(self, nombre):
        super().__init__(nombre) # Hacemos la vinculacion con la "Superclase" al inicializarla y pasarle los parametros

    def avanzar(self):  # Aplico "Polimorfismo" al estrablecer un nuevo comportamiento con el metedo "Avanzar"
        print('Estoy avanando en mi bicicleta')



def run():
    persona = Persona('David') # Creamos nuestro objeto "persona"
    persona.avanzar() 

    ciclista = Ciclista('Mateo')
    ciclista.avanzar() # Este metodo sera distinto al primero que declaramos porque aplicamos "polimorfismo"


if __name__ == '__main__':
    run()