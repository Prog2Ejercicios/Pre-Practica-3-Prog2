# Se desea crear un programa que simule el funcionamiento basico de un vehiculo.
# -Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
# -Crear su constructor
# -Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
# -crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
# -Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


# Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.

# Comisión : 3 TN
# Grupo    : 2
# Integrantes: Azul Cura Ulises Aguirre Nicolas Casa
# -Legajo 50539
# -Legajo 50484
class Vehiculo(): 

    def __init__(self, marca, rueda, color, enMarcha=False): 
        self.marca = marca 
        self.rueda = rueda
        self.color = color
        self.enMarcha = enMarcha

    def arrancar(self):
        self.enMarcha = True
        print("Vehiculo en marcha")

    def tipoVehiculo(self):
        if self.rueda == 4:
            print("Es un Automovil")
        elif self.rueda == 2:
            print("Es una motocicleta")

    def mostrar(self):
        print(self.marca)
        print(self.rueda)    
        print(self.color)       
        print(self.enMarcha)




A = Vehiculo("Ford", 4, "Black")
A.arrancar()
A.tipoVehiculo()
A.mostrar()
m = Vehiculo("Motomel", 2, "fuego_rojo")
m.tipoVehiculo()
m.mostrar()











