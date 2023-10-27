from cliente import Cliente
from tipoCuenta import CajaAhorroDolar, CajaAhorroPeso, CuentaCorrientePeso, CuentaInversion
from tipoTarjeta import TarjetaCredito, TarjetaDebito

# Clase hija de Cliente con las implementaciones que les corresponde a "BLACK".
class ClienteBlack(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni, "BLACK", transacciones)
        tarjeta_debito = TarjetaDebito()
        self.cantidad_tarjetas_debito = 5
        tarjeta_credito_visa = TarjetaCredito("VISA")
        tarjeta_credito_mastercard = TarjetaCredito("MASTERCARD")
        tarjeta_credito_amex = TarjetaCredito("AMEX")
        self.agregar_tarjeta_debito(tarjeta_debito)
        self.agregar_tarjeta_credito(tarjeta_credito_visa)
        self.agregar_tarjeta_credito(tarjeta_credito_mastercard)
        self.agregar_tarjeta_credito(tarjeta_credito_amex)
        self.cantidad_extensiones = 10
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
        if transaccion["tipo"].find("VISA") != -1:
            if transaccion["cantTarjetasDisponibles"] > self.cantidad_extensiones or transaccion["cantTarjetasDisponibles"] == 0:
                return "Excede la cantidad de altas de tarjeta VISA disponibles."
        if transaccion["tipo"].find("MASTERCARD") != -1:
            if transaccion["cantTarjetasDisponibles"] > self.cantidad_extensiones or transaccion["cantTarjetasDisponibles"] == 0:
                return "Excede la cantidad de altas de tarjeta MASTERCARD disponibles."
        if transaccion["tipo"].find("AMEX") != -1:
            if transaccion["cantTarjetasDisponibles"] > self.cantidad_extensiones or transaccion["cantTarjetasDisponibles"] == 0:
                return "Excede la cantidad de altas de tarjeta AMEX disponibles."

    def procesar_alta_chequera(self, transaccion):
        if transaccion["cantChequerasDisponibles"] == 0:
            return "Excede la cantidad de chequeras que puede disponer."
    
    def procesar_compra_dolar(self, transaccion):
        monto = Cliente.calcular_monto_total(self, transaccion)
        if monto > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee saldo suficiente para la compra en dólares."
        
    def procesar_venta_dolar(self, transaccion):
        if transaccion["monto"] > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee saldo suficiente para la venta de dólares."

    def procesar_alta_cuenta_corriente(self, transaccion):
        if transaccion["cantCuentasDisponibles"] != 3:
            return "El cliente BLACK solo puede poseer tres cuentas corrientes."
        
    def procesar_alta_caja_ahorro(self, transaccion):
        if transaccion["cantCuentasDisponibles"] != 5:
            return "El cliente BLACK solo puede poseer cinco cajas de ahorro."
    
    def procesar_alta_cuenta_inversion(self, transaccion):
        if transaccion["cantCuentasDisponibles"] != 1:
            return "El cliente BLACK solo puede poseer una cuenta de inversion."
        
    def procesar_transferencia_enviada(self, transaccion):
        if transaccion["monto"] > transaccion["saldoDisponibleEnCuenta"] or transaccion["monto"] > transaccion["permitidoActualParaTransaccion"]:
            return "No posee el saldo suficiente para la transferencia."
    
    def procesar_transferencia_recibida(self, transaccion):
        if len(self.cuentas) == 0:
            return "El cliente BLACK no tiene una cuenta habilitada para recibir la transferencia."
        
    switch = {
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
        "ALTA_CUENTA_CTE_PESOS": procesar_alta_cuenta_corriente,
        "ALTA_CUENTA_CTE_DOLARES": procesar_alta_cuenta_corriente,
        "ALTA_CAJA_DE_AHORRO_PESOS": procesar_alta_caja_ahorro,
        "ALTA_CAJA_DE_AHORRO_DOLARES": procesar_alta_caja_ahorro,
        "ALTA_CUENTA_DE_INVERSION": procesar_alta_cuenta_inversion,
        "COMPRA_DOLAR": procesar_compra_dolar,
        "VENTA_DOLAR": procesar_venta_dolar,
        "TRANSFERENCIA_ENVIADA_PESOS": procesar_transferencia_enviada,
        "TRANSFERENCIA_ENVIADA_DOLARES": procesar_transferencia_enviada,
        "TRANSFERENCIA_RECIBIDA_PESOS": procesar_transferencia_recibida,
        "TRANSFERENCIA_RECIBIDA_DOLARES": procesar_transferencia_recibida,
    }