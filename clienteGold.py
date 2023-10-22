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
        if transaccion["tipo"].find("AMEX") != -1:
            return "El cliente GOLD no posee tarjeta de credito AMEX."
        
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
       # "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": procesar_retiro_efectivo_cajero_automatico,
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