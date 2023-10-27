# Clase para tomar los valores del archivo Json.
class Transaccion:
    def __init__(self, estado, tipo, cuenta_numero, permitido_actual, monto, fecha, numero, saldo_disponible, cant_tarjetas, cant_chequeras, cant_cuentas, interes):
        self.estado = estado
        self.tipo = tipo
        self.cuenta_numero = cuenta_numero
        self.permitido_actual = permitido_actual
        self.saldo_disponible = saldo_disponible
        self.cant_tarjetas = cant_tarjetas
        self.cant_chequeras = cant_chequeras
        self.cant_cuentas = cant_cuentas
        self.interes = interes
        self.monto = monto
        self.fecha = fecha
        self.numero = numero