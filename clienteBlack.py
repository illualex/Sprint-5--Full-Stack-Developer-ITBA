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

    def procesar_compra_cuotas_tarjeta_credito(self, transaccion):
        partes = transaccion["tipo"].split("_")
        nombre_tarjeta = partes[-1]
        if transaccion["monto"] > self.limite_cuotas:
            return "La tarjeta " + nombre_tarjeta + " excede el limite en cuotas."
        
    def procesar_compra_un_pago_tarjeta_credito(self, transaccion):
        partes = transaccion["tipo"].split("_")
        nombre_tarjeta = partes[-1]
        if transaccion["monto"] > self.limite_un_pago:
            return "La tarjeta " + nombre_tarjeta + " excede el limite en un pago."

    def procesar_alta_tarjeta_credito(self, transaccion):
        #FALTA INFORMACIÓN.
        #posible rechazo falta información.
        pass

    def procesar_alta_chequera(self, transaccion):
        #FALTA INFORMACIÓN.
        pass
    
    def procesar_compra_dolar(self, transaccion):
        monto = Cliente.calcular_monto_total(self, transaccion)
        if monto > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee saldo suficiente para la compra en dólares."
        
    def procesar_venta_dolar(self, transaccion):
        if transaccion["monto"] > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee saldo suficiente para la venta de dólares."

    switch = {
        #"RETIRO_EFECTIVO_POR_CAJA": procesar_retiro_efectivo_por_caja,
        "COMPRA_EN_CUOTAS_TARJETA_CREDITO_VISA": procesar_compra_cuotas_tarjeta_credito,
        "COMPRA_EN_CUOTAS_TARJETA_CREDITO_MASTERCARD": procesar_compra_cuotas_tarjeta_credito,
        "COMPRA_EN_CUOTAS_TARJETA_CREDITO_AMEX": procesar_compra_cuotas_tarjeta_credito,
        "COMPRA_TARJETA_CREDITO_VISA": procesar_compra_un_pago_tarjeta_credito,
        "COMPRA_TARJETA_CREDITO_MASTERCARD": procesar_compra_un_pago_tarjeta_credito,
        "COMPRA_TARJETA_CREDITO_AMEX": procesar_compra_un_pago_tarjeta_credito,
        "ALTA_TARJETA_CREDITO_VISA": procesar_alta_tarjeta_credito,
        "ALTA_TARJETA_CREDITO_MASTERCARD": procesar_alta_tarjeta_credito,
        "ALTA_TARJETA_CREDITO_AMEX": procesar_alta_tarjeta_credito,
        "ALTA_CHEQUERA": procesar_alta_chequera,
        #"ALTA_CUENTA_CTE": procesar_alta_cuenta_corriente,
        #"ALTA_CAJA_DE_AHORRO": procesar_alta_caja_ahorro,
        #"ALTA_CUENTA_DE_INVERSION": procesar_alta_cuenta_inversion,
        "COMPRA_DOLAR": procesar_compra_dolar,
        "VENTA_DOLAR": procesar_venta_dolar,
        #"TRANSFERENCIA_ENVIADA": procesar_transferencia_enviada,
        #"TRANSFERENCIA_RECIBIDA": procesar_transferencia_recibida,
    }

