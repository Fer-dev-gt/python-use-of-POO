# Declaro mi primera clase llamada "Persona" (con mayuscula) con el método "__init__" y el metodo "saludar"
def run():
    class Persona:
        # Cuando se crea una instancia, se ejecuta el método "__init__"
        def __init__(self, nombre, edad): # "Self" es un referencia a las instancias que voy a crear, recibe parametros cuando se crea un nuevo objeto 

            self.nombre = nombre    # Aqui creo mis atributos usando el mismo nombre de los parametros recibidos
            self.edad = edad

        def saludar(self, otra_persona): # Esto es un "Método" el cual contienen todos los objetos que voy a crear
            return print(f'Hola {otra_persona}, me llamo {self.nombre}.')

    # Uso o invocación de mi clase, tambien conocido como "Inicializando una instacia de una clase"

    david = Persona('David', 35) # AQUI ES DONDE ESTOY CREANDO UN NUEVO OBJETO, que almacena lo establecido en mi clase "Persona" y le mando dos argumentos correspondientes a lo que ya habia declarado

    erika = Persona('Erika', 32) # Creo otro objeto llamado "Erika" que contiene datos o "atributos" diferentes

    # Aqui ejecutamos los "Métodos" de mi clase "Persona", ya que "david" al ser objeto de la clase "Persona" tiene acceso a los Métodos declarados en esa clase

    david.saludar(erika)


if __name__ == '__main__':
    run()
