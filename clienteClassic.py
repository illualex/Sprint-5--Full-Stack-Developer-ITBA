from cliente import Cliente
from tipoCuenta import CajaAhorroPeso
from tipoTarjeta import TarjetaDebito

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

    def procesar_compra_cuotas_tarjeta_credito(self, transaccion):
        return "El cliente CLASSIC no posee beneficio para usar tarjetas de crédito."

    def procesar_compra_un_pago_tarjeta_credito(self, transaccion):
        return "El cliente CLASSIC no posee beneficio para usar tarjetas de crédito."

    def procesar_retiro_efectivo_cajero_automatico(self, transaccion):
        if (transaccion["saldoDisponibleEnCuenta"] < transaccion["monto"]) or (transaccion["monto"] > self.limite_retiro_diario):
            return "El cliente no dispone de saldo suficiente para retirar en cajero."

    def procesar_alta_tarjeta_credito(self, transaccion):
        return "El cliente CLASSIC no posee beneficios para alta en tarjeta de crédito."

    def procesar_alta_chequera(self, transaccion):
        return "El cliente CLASSIC no posee beneficios para chequera."
    
    def procesar_compra_dolar(self, transaccion):
        return "El cliente no posee caja de ahorro en dólares."
    
    def procesar_venta_dolar(self, transaccion):
        return "El cliente no posee caja de ahorro en dólares."

    switch = {
        "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": procesar_retiro_efectivo_cajero_automatico,
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
