# Clase para determinar el tipo de cuenta.
class TipoCuenta:
    def __init__(self, nombre):
        self.nombre = nombre

class CajaAhorroPeso(TipoCuenta):
    def __init__(self):
        super().__init__("Caja de ahorro en pesos")

class CajaAhorroDolar(TipoCuenta):
    def __init__(self):
        super().__init__("Caja de ahorro en dólares")

class CuentaCorrientePeso(TipoCuenta):
    def __init__(self):
        super().__init__("Cuenta Corriente en pesos")

class CuentaCorrienteDolar(TipoCuenta):
    def __init__(self):
        super().__init__("Cuenta Corriente en dólares")

class CuentaInversion(TipoCuenta):
    def __init__(self):
        super().__init__("Cuenta Inversión")