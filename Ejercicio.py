'''
Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.
Comisión : X
Grupo : X
Integrantes:
-Legajo XXXX,....
-Legajo YYYY,....
.
.
.

'''

class vehiculo():
    #precio=250 es una variable de clase, para todos vale lo mismo
                    #type hints es definir el tipo ejemplo: color (str) pero no hace falta
    def __init__(self, marca, ruedas, color, enMarcha=False):  #SI PIDE EL ENUNCIADO QUE RESPONDA AL ENMARCHA SIN DEFINIR EL BOOLEANO POR DEFECTO
        self.marca=marca                                 #SE PONE ENMARCHA=FALSE O SI QUIERE POR DEFECTO TRUE, SE PONE ENMARCHA = TRUE
        self.ruedas=ruedas
        self.color=color
        self.enMarcha=enMarcha      #Variables de instancia

    def arrancar(self):
        self.enMarcha=True
    
    def tipoVehiculo(self):
        if (self.ruedas == 4):
            return "Automovil"
        else: 
            return"Motocicleta"
    def mostrar(self):
        print(self.marca)
        print(self.ruedas)              #Def metodos de instancia
        print(self.color)
        print(self.enMarcha)


#DEFINICION DE AUTOS
auto_1=vehiculo("Ford", 4,"Azul", False)
auto_2=vehiculo("Toyota", 2,"Verde", False)

auto_1.mostrar()
auto_2.mostrar()

