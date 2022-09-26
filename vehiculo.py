class Vehiculo():

    def __init__(self, marca, ruedas, color, enMarcha=False):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha

    def arrancar(self):
        self.enMarcha = True

    def tipoVehiculo(self):
        if(self.ruedas == 4):
            return 'Automovil'
        else:
            return "Moto"

    def mostrar(self):
        print(self.marca)
        print(self.ruedas)
        print(self.color)
        print(self.enMarcha)


auto_1 = Vehiculo("Ford", 4, "Azul", False)

auto_1.arrancar()

print(auto_1.tipoVehiculo())

auto_1.mostrar()