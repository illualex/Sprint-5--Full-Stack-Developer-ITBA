from cliente import Cliente
from tipoCuenta import CajaAhorroPeso
from tipoTarjeta import TarjetaDebito
from funciones import calcular_monto_total, descontar_comision, calcular_monto_plazo_fijo


class ClienteClassic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni, "CLASSIC", transacciones)
        tarjeta_debito = TarjetaDebito()
        self.agregar_tarjeta_debito(tarjeta_debito)
        self.cantidad_tarjetas_debito = 1
        caja_ahorro_peso = CajaAhorroPeso()
        self.agregar_cuenta(caja_ahorro_peso)
        self.limite_retiro_diario = 10000
        self.cantidad_retiro_diario = 5
        self.comision_transferencia_saliente = 1
        self.comision_transferencia_entrante = 0.5

    def calcular_monto_total(self, precio_dolar, monto):
        impuesto_pais = 0.30  # Impuesto país del 30%
        ganancias = 0.35  # Ganancias del 35%
        total = monto * precio_dolar
        total += total * impuesto_pais
        total += total * ganancias
        return total

    def descontar_comision(self, monto, comision_porcentaje):
        comision = monto * comision_porcentaje
        return monto - comision

    def calcular_monto_plazo_fijo(self, monto, interes):
        return monto * (1 + (interes / 100))
    
    

    
