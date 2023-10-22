class Transaccion:
    def __init__(self, estado, tipo, cuenta_numero, permitido_actual, monto, fecha, numero):
        self.estado = estado
        self.tipo = tipo
        self.cuenta_numero = cuenta_numero
        self.permitido_actual = permitido_actual
        self.monto = monto
        self.fecha = fecha
        self.numero = numero