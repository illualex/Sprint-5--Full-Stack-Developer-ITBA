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
            # Simplemente llama a la función calcular_monto_total de funciones.py
            return calcular_monto_total(precio_dolar, monto)

    def descontar_comision(self, monto, comision_porcentaje):
        return descontar_comision(monto,comision_porcentaje)

    def calcular_monto_plazo_fijo(self, monto, interes):
        return calcular_monto_plazo_fijo(self, monto, interes)
    
    

    
