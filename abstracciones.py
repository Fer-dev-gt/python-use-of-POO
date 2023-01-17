"""En este programa implementaremos el concepto de "Abstraccion" donde separamos la informacion importante de la secundaria usando variables/métodos privados """

class Lavadora:

    def __init__(self): # Como estamos usando variables privadas, no es necesario ingresar parametros del usuario
        pass

        # Este Método va llamar internamente a otro métodos privados (Cosas que no le interesan al usuario y que no van en la interfaz) 
    def lavar(self, temperatura = 'caliente'): # Creamos un metodo publico de lo que significa lavar
        # Usamos variables privadas, porque al usuario no le interesa como funciona internamente la lavadora
        self._llenar_tanque_de_agua(temperatura) # Estos son "Métodos que abajo vamos a definir"
        self._anadir_jabon()
        self._lavar()
        self._centrifugar() 


    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabón')

    def _lavar(self): # Ya que este Método tiene un "_" al inicio significa que es disitinto al metodo "lavar" de arriba
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()


"""Un claro ejemplo de la Abstraccion se puede ver al aplicar formulas de Fisica, podemos irnos a los detalles y analizar como se mueven las particulas subatomicas, o podemos usar una formular para dejar esos detalles afuera y solo nos preocupamos por los datos de entrada y salida que ingrese el usuario como con la formula 'Fuerza = masa * aceleracion'"""