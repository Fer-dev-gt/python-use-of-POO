# Esta clase utiliza los conceptos de "getters y setters" con la notacion de "decorators" usando el simbolo "@"

class CasillaDeVotacion:

    def __init__(self, identificador, pais):  
        self._identificador = identificador  # Utilizamos variables de instancia privadas
        self._pais = pais
        self._region = None # "__region" no recibi parametro al inicio eso lo ingresaremos despues

        # Esto es un "getter"
        @property  # Aqui empezamos a establecer las condiciones para tener acceso a los siguiente metodos
        def region(self):
            return self._region


        # Esta funcion no permite modificar el valor anterior en "@property" usando su nombre de prepiedad junto al ".setter"   
        @region.setter  
        def region(self, region):
            if region in self._pais:
                self._region = region
            else:   # Aqui declaramoe un "raise" fuera el caso que la region no este registrada en la lista
                raise ValueError(f'La region {region} no es valida en {self._pais}')


casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
print(casilla._region)
casilla._region = 'Mexico'
print(casilla._region)


