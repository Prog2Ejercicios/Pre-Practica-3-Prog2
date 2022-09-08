# Se desea crear un programa que simule el funcionamiento basico de un vehiculo.
# -Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
# -Crear su constructor
# -Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
# -crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
# -Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


# Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.

# Comisión : 4 
# Grupo    : 9
# Integrantes: Bruno Menna, Guido Montenegro, Nihuel Spinelli, Francisco Urquiza
# -Legajo 50625, Bruno Menna
# -Legajo 50622, Guido Montenegro
# -Legajo 50512, Nihuel Spinelli
# -Legajo 50505, Francisco Urquiza

class Vehiculo:
    def __init__(self, marca, color, ruedas, enMarcha=False):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
        self.enMarcha = enMarcha

    def arrancar(self):
        
        if self.enMarcha == True:
            print("En marcha")
        elif self.enMarcha == False:
            print("Detenido")

    def tipoVehiculo(self):
        if self.ruedas == 4:
            print("Automovil")
        elif self.ruedas == 2:
            print("Motocicleta")


    def mostrar(self):
        print("Marca: " ,self.marca)
        print("Color: ", self.color)
        print("Ruedas: ", self.ruedas)
        print("En marcha: ", self.enMarcha)

p208 = Vehiculo("Peugeot 208", "Rojo", 4, True)

p208.arrancar()

p208.tipoVehiculo()

p208.mostrar()


Honda = Vehiculo("Honda", "Verde", 2, False)

Honda.arrancar()

Honda.tipoVehiculo()

Honda.mostrar()