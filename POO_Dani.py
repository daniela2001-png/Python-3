#self es el mismo objeto que creamos apartir de la clase ejemplo:
class Daniela():
    edad = 18 
    peso = 50
    Despierta = False
    
    def despertar(self):
        self.Despierta = True
    def estado_de_dani(self):
        if (self.Despierta):
            return "dani se levanto"
        else:
            return "sigo durmiendo jajaj"
Dani = Daniela()
print(Dani.edad)
print(Dani.Despierta)
Dani.despertar()
print(Dani.Despierta)
print(Dani.estado_de_dani())
#nota final: nuestra clase Daniela tiene 3 atributos  o propiedades que vendriansç siendo variables de clase o estaicas!
# tiene dos metodos o comoprtamiento o instancias publicas
