class Vehiculo():
    marca = str
    ruedas = int
    color = str
    enMarcha = bool

    def init(self, marca,ruedas,color,enMarcha=False):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha

    def arrancar(self,enMarcha=False):
        self.enMarcha = True
        print("Arrancando el "+self.marca+" de color: "+self.color)

    def tipoVehiculo(self):
        if self.ruedas == 2:
            return print("Motocicleta")
        elif self.ruedas == 4:
            return print("Automovil")
        else:
            return print("Nuestro vehículo no es ni un automovil ni una motocicleta")

    def mostrar(self):
        if self.ruedas == 2:
            print("Nuestra Motocicleta es de marca: "+self.marca+" color: "+self.color)
        elif self.ruedas == 4:
            print("Nuestro Automovil es de marca: "+self.marca+" color: "+self.color)
        
        if self.enMarcha == True:
            print("Nuestro vehículo se encuentra en marcha")
        else:
            print("Nuestro vehículo no se encuentra en marcha")

miAuto=Vehiculo()
miAuto.init('Ferrari',4,'Rojo',True)
miAuto.arrancar()
miAuto.tipoVehiculo()
miAuto.mostrar()