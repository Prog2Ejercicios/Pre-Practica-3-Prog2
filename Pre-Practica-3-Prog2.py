"""Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


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
."""

from __future__ import annotations


class Vehiculo:
    marca = ""
    ruedas = 0
    color = ""
    enMarcha = False

    def __init__(self, marca, ruedas, color) -> None:
        self.marca = marca
        self.ruedas = ruedas
        self.color = color

    def arrancar(self) -> bool:
        self.enMarcha = True

    def tipoVehiculo(self) -> str:
        if self.ruedas == 4:
            print("Automovil")
        if self.ruedas == 2:
            print("Motocicleta")

    def mostrar(self):
        print("Marca: " + self.marca)
        print("Ruedas: ", self.ruedas)
        print("Color: " + self.color)
        print("Encendido: ", self.enMarcha)


ferrari = Vehiculo("Ferrari", 4, "Rojo")
ferrari.mostrar()
ferrari.arrancar()
ferrari.mostrar()
""""
Comisión : 4
Grupo : 1
Integrantes: Franco Romero, Leonel Zarini, Virginia Vaccaro, Juan Ignacio Moyano

"""
