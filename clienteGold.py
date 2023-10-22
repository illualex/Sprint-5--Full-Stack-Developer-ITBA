from cliente import Cliente
from tipoCuenta import CajaAhorroDolar, CajaAhorroPeso, CuentaCorrientePeso
from tipoTarjeta import TarjetaCredito, TarjetaDebito

class ClienteGold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni, "GOLD", transacciones)
        tarjeta_debito = TarjetaDebito()
        self.cantidad_tarjetas_debito = 1
        tarjeta_credito_visa = TarjetaCredito("VISA", 5)  # Ejemplo de tarjeta de crédito VISA
        tarjeta_credito_mastercard = TarjetaCredito("MASTERCARD", 5)  # Ejemplo de tarjeta de crédito MASTERCARD
        self.agregar_tarjeta_debito(tarjeta_debito)
        self.agregar_tarjeta_credito(tarjeta_credito_visa)
        self.agregar_tarjeta_credito(tarjeta_credito_mastercard)
        caja_ahorro_peso = CajaAhorroPeso()
        caja_ahorro_dolares = CajaAhorroDolar()
        cuenta_corriente_peso = CuentaCorrientePeso()
        self.cajas_ahorro_dolares = 1
        self.agregar_cuenta(caja_ahorro_peso)
        self.agregar_cuenta(cuenta_corriente_peso)
        self.agregar_cuenta(caja_ahorro_dolares)
        self.cuenta_corriente = 1
        self.limite_retiro_diario = 20000
        self.limite_un_pago = 150000
        self.limite_cuotas = 100000
        self.comision_transferencia_saliente = 0.5
        self.comision_transferencia_entrante = 0.1
        self.cuentas_inversion = 1
        self.chequeras = 1

    def aplicar_restricciones(self):
        if self.cajas_ahorro_dolares > 2:
            # Aplicar cargo mensual adicional por cajas de ahorro en dólares adicionales
            self.comision_transferencia_entrante += 0.001
            self.comision_transferencia_saliente += 0.005

        if len(self.tarjetas_debito) > 1:
            # Limitar a una tarjeta de débito
            self.tarjetas_debito = self.tarjetas_debito[:1]

        if len(self.tarjetas_credito) > 5:
            # Limitar a 5 tarjetas de crédito
            self.tarjetas_credito = self.tarjetas_credito[:5]

        if self.limite_retiro_diario > 20000:
            # No hay límite para retiros diarios sin comisiones
            self.limite_retiro_diario = 0

        # Implementar las demás restricciones específicas para el cliente Gold

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
  
    def procesar_compra_tarjeta_credito(self, transaccion):
       if transaccion.tipo.find("VISA") != -1:
            if transaccion.monto > self.limite_un_pago:
                return "Excede el limite en un pago"
