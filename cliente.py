from resumen import Resumen

class Cliente:
    def __init__(self, numero, nombre, apellido, dni, tipo, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.transacciones = []
        self.tarjetas_debito = []
        self.cantidad_tarjetas_debito = 0
        self.cajas_ahorro_pesos = 1
        self.cajas_ahorro_dolares = 0
        self.cuenta_corriente = 0
        self.tarjetas_credito = []
        self.cuentas = []
        self.limite_retiro_diario = 0
        self.limite_un_pago = 0
        self.limite_cuotas = 0
        self.comision_transferencia_saliente = 0.0
        self.comision_transferencia_entrante = 0.0
        self.cuentas_inversion = 0
        self.chequeras = 0
        self.transacciones = transacciones


    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def agregar_tarjeta_debito(self, tarjeta):
        self.tarjetas_debito.append(tarjeta)

    def agregar_tarjeta_credito(self, tarjeta):
        self.tarjetas_credito.append(tarjeta)

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    #SWITCH
    def procesar_retiro_efectivo_cajero_automatico(self, transaccion):
        # Implementa el procesamiento para RETIRO_EFECTIVO_CAJERO_AUTOMATICO aquí
        pass

    def procesar_retiro_efectivo_por_caja(self, transaccion):
        # Implementa el procesamiento para RETIRO_EFECTIVO_POR_CAJA aquí
        pass
    
    def procesar_compra_tarjeta_credito(self, transaccion):
        pass
   
    def procesar_alta_tarjeta_credito(self, transaccion):
        pass

    def procesar_alta_tarjeta_debito(self, transaccion):
        pass
    def procesar_alta_chequera(self, transaccion):
        pass
    def procesar_alta_cuenta_corriente(self, transaccion):
        pass
    def procesar_alta_caja_ahorro(self, transaccion):
        pass
    def procesar_alta_cuenta_inversion(self, transaccion):
        pass
    def procesar_compra_dolar(self, transaccion):
        pass
    def procesar_venta_dolar(self, transaccion):
        pass
    def procesar_transferencia_enviada(self, transaccion):
        pass
    def procesar_transferencia_recibida(self, transaccion):
        pass

    switch = {
        "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": procesar_retiro_efectivo_cajero_automatico,
        "RETIRO_EFECTIVO_POR_CAJA": procesar_retiro_efectivo_por_caja,
        "COMPRA_EN_CUOTAS_TARJETA_CREDITO_VISA": procesar_compra_tarjeta_credito,
        "COMPRA_EN_CUOTAS_TARJETA_CREDITO_MASTERCARD": procesar_compra_tarjeta_credito,
        "COMPRA_EN_CUOTAS_TARJETA_CREDITO_AMEX": procesar_compra_tarjeta_credito,
        "COMPRA_TARJETA_CREDITO": procesar_compra_tarjeta_credito,
        "ALTA_TARJETA_CREDITO": procesar_alta_tarjeta_credito,
        "ALTA_TARJETA_DEBITO": procesar_alta_tarjeta_debito,
        "ALTA_CHEQUERA": procesar_alta_chequera,
        "ALTA_CUENTA_CTE": procesar_alta_cuenta_corriente,
        "ALTA_CAJA_DE_AHORRO": procesar_alta_caja_ahorro,
        "ALTA_CUENTA_DE_INVERSION": procesar_alta_cuenta_inversion,
        "COMPRA_DOLAR": procesar_compra_dolar,
        "VENTA_DOLAR": procesar_venta_dolar,
        "TRANSFERENCIA_ENVIADA": procesar_transferencia_enviada,
        "TRANSFERENCIA_RECIBIDA": procesar_transferencia_recibida,
    }
    
    def procesar_transaccion(self):
        # Implementar restricciones específicas en las clases derivadas
        resumen_completo = []
    
        for transaccion in self.transacciones:
            if transaccion["estado"] == "RECHAZADA":
                
                # Obtén la función correspondiente a la transacción
                funcion = self.switch.get(transaccion.get("tipo"))

                if funcion:
                    motivo = funcion(self, transaccion)
                    resumen = Resumen(transaccion["estado"], transaccion["tipo"], transaccion["fecha"], transaccion["numero"], motivo)
                    resumen_completo.append(resumen)
                else:
                    print(f"Operación no reconocida: {transaccion.get('tipo')}")
            else:
                resumen = Resumen(transaccion["estado"], transaccion["tipo"], transaccion["fecha"], transaccion["numero"], "Operación aceptada.")
                resumen_completo.append(resumen)

        return resumen_completo

    

    





