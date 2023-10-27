from cliente import Cliente
from tipoCuenta import CajaAhorroDolar, CajaAhorroPeso, CuentaCorrientePeso
from tipoTarjeta import TarjetaCredito, TarjetaDebito

# Clase hija de Cliente con las implementaciones que les corresponde a "GOLD".
class ClienteGold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        super().__init__(numero, nombre, apellido, dni, "GOLD", transacciones)
        tarjeta_debito = TarjetaDebito()
        self.cantidad_tarjetas_debito = 1
        tarjeta_credito_visa = TarjetaCredito("VISA")
        tarjeta_credito_mastercard = TarjetaCredito("MASTERCARD")
        self.agregar_tarjeta_debito(tarjeta_debito)
        self.agregar_tarjeta_credito(tarjeta_credito_visa)
        self.agregar_tarjeta_credito(tarjeta_credito_mastercard)
        self.cantidad_extensiones = 5
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
        self.comision_transferencia_saliente = 0.005
        self.comision_transferencia_entrante = 0.001
        self.cuentas_inversion = 1
        self.chequeras = 1
        
    def procesar_compra_cuotas_tarjeta_credito(self, transaccion):
        if transaccion["tipo"].find("VISA") != -1:
            if transaccion["monto"] > self.limite_cuotas:
                return "La tarjeta VISA excede el limite en cuotas."
        if transaccion["tipo"].find("MASTERCARD") != -1:
           if transaccion["monto"] > self.limite_cuotas:
               return "La tarjeta MASTERCARD excede el limite en cuotas."
        if transaccion["tipo"].find("AMEX") != -1:
           return "El cliente GOLD no posee beneficio para usar tarjeta AMEX."
        
    def procesar_compra_un_pago_tarjeta_credito(self, transaccion):
        if transaccion["tipo"].find("VISA") != -1:
            if transaccion["monto"] > self.limite_un_pago:
                return "La tarjeta VISA excede el limite en un pago."
        if transaccion["tipo"].find("MASTERCARD") != -1:
           if transaccion["monto"] > self.limite_un_pago:
               return "La tarjeta MASTERCARD excede el limite en un pago."
        if transaccion["tipo"].find("AMEX") != -1:
           return "El cliente GOLD no posee beneficio para usar tarjeta AMEX."

    def procesar_alta_tarjeta_credito(self, transaccion):
        if transaccion["tipo"].find("VISA") != -1:
            if transaccion["cantTarjetasDisponibles"] > self.cantidad_extensiones or transaccion["cantTarjetasDisponibles"] == 0:
                return "Excede la cantidad de altas de tarjeta VISA disponibles."
        if transaccion["tipo"].find("MASTERCARD") != -1:
            if transaccion["cantTarjetasDisponibles"] > self.cantidad_extensiones or transaccion["cantTarjetasDisponibles"] == 0:
                return "Excede la cantidad de altas de tarjeta MASTERCARD disponibles."
        if transaccion["tipo"].find("AMEX") != -1:
            return "El cliente GOLD no posee tarjeta de credito AMEX."
        
    def procesar_alta_chequera(self, transaccion):
        if transaccion["cantChequerasDisponibles"] > self.chequeras or transaccion["cantChequerasDisponibles"] == 0:
            return "Excede la cantidad de chequeras que puede disponer."
    
    def procesar_compra_dolar(self, transaccion):
        monto = Cliente.calcular_monto_total(self, transaccion)
        if monto > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee saldo suficiente para la compra en dólares."
    
    def procesar_venta_dolar(self, transaccion):
        if transaccion["monto"] > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee saldo suficiente para la venta de dólares."
        
    def procesar_alta_cuenta_corriente(self, transaccion):
        if transaccion["cantCuentasDisponibles"] != 1:
            return "El cliente GOLD solo puede poseer una cuenta corriente."
        
    def procesar_alta_caja_ahorro(self, transaccion):
        if transaccion["cantCuentasDisponibles"] != 1:
            return "El cliente GOLD solo puede poseer una caja de ahorro."
        
    def procesar_alta_cuenta_inversion(self, transaccion):
        if transaccion["cantCuentasDisponibles"] != 1:
            return "El cliente GOLD solo puede poseer una cuenta de inversion."
        
    def procesar_transferencia_enviada(self, transaccion):
        descontar_comision = Cliente.descontar_comision(self, transaccion["monto"], self.comision_transferencia_saliente)
        if transaccion["permitidoActualParaTransaccion"] < descontar_comision:
            return "No posee el saldo suficiente para la transferencia."
        
    def procesar_transferencia_recibida(self, transaccion):
        if len(self.cuentas) == 0:
            return "El cliente GOLD no tiene una cuenta habilitada para recibir la transferencia."


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