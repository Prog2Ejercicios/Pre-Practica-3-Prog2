class Vehiculo:
    marca = str
    ruedas = int
    color = str
    enMarcha = False

    def arrancar(self):
        self.enMarcha=True
    def estado(self):
        if(self.enMarcha==True):
            return "El vehiculo esta en marcha"
        else:
        return "El vehiculo esta apagado"