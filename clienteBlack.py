from cliente import Cliente
from tipoCuenta import CajaAhorroDolar, CajaAhorroPeso, CuentaCorrientePeso, CuentaInversion
from tipoTarjeta import TarjetaCredito, TarjetaDebito

class ClienteBlack(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni, "BLACK", transacciones)
        tarjeta_debito = TarjetaDebito()
        self.cantidad_tarjetas_debito = 5
        tarjeta_credito_visa = TarjetaCredito("VISA", 10)  # Ejemplo de tarjeta de crédito VISA
        tarjeta_credito_mastercard = TarjetaCredito("MASTERCARD", 10)  # Ejemplo de tarjeta de crédito MASTERCARD
        tarjeta_credito_amex = TarjetaCredito("AMEX", 10)  # Ejemplo de tarjeta de crédito AMEX (American Express)
        self.agregar_tarjeta_debito(tarjeta_debito)
        self.agregar_tarjeta_credito(tarjeta_credito_visa)
        self.agregar_tarjeta_credito(tarjeta_credito_mastercard)
        self.agregar_tarjeta_credito(tarjeta_credito_amex)
        caja_ahorro_peso = CajaAhorroPeso()
        caja_ahorro_dolar = CajaAhorroDolar()
        self.cajas_ahorro_pesos = 5
        self.cajas_ahorro_dolares = 5
        self.cuenta_corriente = 3
        self.limite_retiro_diario = 100000
        cuenta_corriente_peso = CuentaCorrientePeso()
        cuenta_inversion = CuentaInversion()
        self.agregar_cuenta(caja_ahorro_peso)
        self.agregar_cuenta(caja_ahorro_dolar)
        self.agregar_cuenta(cuenta_corriente_peso)
        self.agregar_cuenta(cuenta_inversion)
        self.comision_transferencia_saliente = 0.0
        self.comision_transferencia_entrante = 0.0
        self.cuentas_inversion = 1
        self.chequeras = 2


    def aplicar_restricciones(self):
        if self.cajas_ahorro_pesos > 5 or self.cajas_ahorro_dolares > 5:
            # Aplicar cargo mensual adicional por exceso de cajas de ahorro
            self.comision_transferencia_entrante += 0.005
            self.comision_transferencia_saliente += 0.01

        if self.cuenta_corriente > 3:
            # Limitar a 3 cuentas corrientes
            self.cuenta_corriente = 3

        if len(self.tarjetas_debito) > 5:
            # Limitar a 5 tarjetas de débito
            self.tarjetas_debito = self.tarjetas_debito[:5]

        if len(self.tarjetas_credito) > 10:
            # Limitar a 10 tarjetas de crédito
            self.tarjetas_credito = self.tarjetas_credito[:10]

        if self.limite_retiro_diario > 100000:
            # No hay límite para retiros diarios sin comisiones
            self.limite_retiro_diario = 0

        if self.chequeras > 2:
            # Limitar a 2 chequeras
            self.chequeras = 2

        # Implementar las demás restricciones específicas para el cliente Black

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
    
    def procesar_transaccion(self):
        pass  # Implementar restricciones específicas en las clases derivadas