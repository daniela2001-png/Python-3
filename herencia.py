# superclase que va ser la que tine todo lo comun entre mis objetos computadores

class computadores():
    
    # constructor que toma dos parametros que tienen en comun nuestros objetos 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.prendido = False
        self.apagado = False
        self.trabajando = False
        
    def estado_prendido(self):
        self.prendido = True
        return self.prendido
    
    def estado_apagado(self):
        self.apagado = True
        return self.apagado
    
    def estado_trabajando(self):
        self.trabajando = True
        return self.trabajando
    
    def estado(self):
        return("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nprendido: ", self.prendido, "\napagado: ", self.apagado, "\ntrabajando: ", self.trabajando)

class portatil(computadores):
    
    def puedo_moverme(self, where):
        self.lugar = where
        if (self.lugar):
            return('soy mas accesible que un pc me puedes mover a donde quieras')
        else:
            return('vamos puedes moverme')
            
    def estado(self): #aqui estamos sobrescribiendo el metodo estado de la superclase
        return("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nprendido: ", self.prendido, "\napagado: ", self.apagado, "\ntrabajando: ", self.trabajando, "\nlugar: ", self.lugar)

    
#class pc(computadores):
 #   pass

print("----computer potatil----")
computer_1 = portatil('hp', '123')
print(computer_1.puedo_moverme('cocina'))
print(computer_1.estado()) #aqui estamos sobrescribiendo el metodo estado de la superclase

#print("----computer pc--------")
#computer_pc = pc("lenovo", "456")
#print(computer_pc.estado())
