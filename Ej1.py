from turtle import clear


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