from cliente import Cliente
from tipoCuenta import CajaAhorroPeso
from tipoTarjeta import TarjetaDebito

# Clase hija de Cliente con las implementaciones que les corresponde a "CLASSIC".
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
        self.comision_transferencia_saliente = 0.01
        self.comision_transferencia_entrante = 0.005

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
    
    def procesar_alta_cuenta_corriente(self, transaccion):
        return "El cliente CLASSIC no puede tener una cuenta corriente."
    
    def procesar_alta_caja_ahorro(self, transaccion):
        if transaccion["tipo"].find("PESOS") != -1:
            if transaccion["cantCuentasDisponibles"] != 1:
                return "El cliente CLASSIC solo puede poseer una caja de ahorro en PESOS."
        if transaccion["tipo"].find("DOLARES") != -1:
            return "El cliente CLASSIC no puede tener una caja de ahorro en DÓLARES."
        
    def procesar_alta_cuenta_inversion(self, transaccion):
        return "El cliente CLASSIC no puede tener una cuenta de inversion."
    
    def procesar_transferencia_enviada(self, transaccion):
        descontar_comision = Cliente.descontar_comision(self, transaccion["monto"], self.comision_transferencia_saliente)
        if transaccion["tipo"].find("PESOS") != -1:
            if transaccion["permitidoActualParaTransaccion"] < descontar_comision:
                return "No posee el saldo suficiente para la transferencia."
        if transaccion["tipo"].find("DOLARES") != -1:
            return "El cliente no posee cuenta en Dólares."
        
    def procesar_transferencia_recibida(self, transaccion):
        if transaccion["tipo"].find("PESOS") != -1:
            if len(self.cuentas) == 0:
                return "El cliente CLASSIC no tiene una cuenta habilitada para recibir la transferencia."
        if transaccion["tipo"].find("DOLARES") != -1:
            return "El cliente CLASSIC no tiene una cuenta en Dólares."

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