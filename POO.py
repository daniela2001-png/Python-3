class Persona:# definimos la clase

    def __init__(self,nom):
        self.nombre=nom #variable de instancia

    def imprimir(self):
        print("Nombre: {0}".format(self.nombre))

#persona1=Persona()
persona1 = Persona("Pedro")
persona1.imprimir()

#persona2=Persona()
persona2 = Persona("Carla")
persona2.imprimir()# aqui accedo directamenete al metodo

#pero si quiero saber de que tipo es cada obejto hago esto con type#
class Persona:

    def __init__(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre: {0}".format(self.nombre))

p1 = Persona("Juan")
p2 = Persona("Pedro")
p1.imprimir()
p2.imprimir()
print(type(Persona))
print(type(p1)) # esto usar type
print(type(p2))