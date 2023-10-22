class TipoTarjeta:
    def __init__(self, nombre, cant_extensiones=0):
        self.nombre = nombre
        self.cant_extensiones = cant_extensiones

    #def agregar_extension(self):
     #   self.cant_extensiones += 1

class TarjetaDebito(TipoTarjeta):
    def __init__(self, nombre="Tarjeta de Débito"):
        super().__init__(nombre, 0)



class TarjetaCredito(TipoTarjeta):
    def __init__(self, nombre, cant_extensiones=0):
        super().__init__("Tarjeta de Crédito " + nombre, cant_extensiones)