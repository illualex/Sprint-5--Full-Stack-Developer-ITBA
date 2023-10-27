# Clase para determinar el tipo de tarjeta.
class TipoTarjeta:
    def __init__(self, nombre):
        self.nombre = nombre

class TarjetaDebito(TipoTarjeta):
    def __init__(self, nombre="Tarjeta de Débito"):
        super().__init__(nombre)

class TarjetaCredito(TipoTarjeta):
    def __init__(self, nombre):
        super().__init__("Tarjeta de Crédito " + nombre)