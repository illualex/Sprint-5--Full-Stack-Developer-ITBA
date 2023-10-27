# Guarda los datos para la salida en HTML según cada operación.
class Resumen:
    def __init__(self, estado, tipo, fecha, numero, motivo):
        self.estado = estado
        self.tipo = tipo
        self.fecha = fecha
        self.numero = numero
        self.motivo = motivo