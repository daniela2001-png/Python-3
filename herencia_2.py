class Persona():

    def __init__(self, nombre, edad, lugar):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar

    def descripcion_persona(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de Residencia: ", self.lugar)

    class Empleado(Persona):

        def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, lugar_empleado):

            super().__init__(nombre_empleado, edad_empleado, lugar_empleado)

            self.salario = salario
            self.antiguedad = antiguedad

        def descripcion_persona(self):

            super().descripcion_persona()

            return(print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad))


persona1 = Empleado(100000, 45, 'daniela', '18', 'usme')
print(persona1.descripcion_persona())
print(isinstance(persona1, Empleado))
print(str(persona1))
