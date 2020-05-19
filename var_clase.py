# Tema "variables de clase":
class Perros:
    'Clase para los perros' #Descripción
    Collar = True #Variable de clase Estática
    def __init__(self, salud, hambre):
        self.salud = salud #Variable de Instancia
        self.hambre = hambre #Variable de Instancia
        
print(Perros.Collar)#asi accedemos a una variable estatica o de clase(solo conla clase)
