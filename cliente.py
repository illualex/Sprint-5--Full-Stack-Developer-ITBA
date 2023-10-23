from resumen import Resumen

class Cliente:
    PRECIO_DOLAR = 1000
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

    def calcular_monto_total(self, transaccion):
        impuesto_pais = 0.30  # Impuesto país del 30%
        ganancias = 0.35  # Ganancias del 35%
        total = transaccion["monto"] * self.PRECIO_DOLAR
        total += total * impuesto_pais
        total += total * ganancias
        return total
    
    def descontar_comision(self, monto, comision_porcentaje):
        comision = monto * comision_porcentaje
        return monto - comision

    def calcular_monto_plazo_fijo(self, monto, interes):
        return monto * (1 + (interes / 100))
    
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
        if (transaccion["saldoDisponibleEnCuenta"] < transaccion["monto"]) or (transaccion["monto"] > self.limite_retiro_diario):
            return "El cliente no dispone de saldo suficiente para retirar en cajero."
        
    def procesar_retiro_efectivo_por_caja(self, transaccion):
        pass
    def procesar_compra_tarjeta_credito(self, transaccion):
        pass
    def procesar_alta_tarjeta_credito(self, transaccion):
        pass
    def procesar_alta_tarjeta_debito(self, transaccion):
        #FALTA INFORMACIÓN.
        #falta saber la cantidad que tiene debito
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
    
    def procesar_transaccion(self):
        # Implementar restricciones específicas en las clases derivadas
        resumen_completo = []
    
        for transaccion in self.transacciones:
            if transaccion["estado"] == "RECHAZADA":
                
                # Obtén la función correspondiente a la transacción
                funcion = self.switch.get(transaccion.get("tipo"))
                if funcion is None:
                    funcion = Cliente.switch.get(transaccion.get("tipo"))
                
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

    switch = {
       "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": procesar_retiro_efectivo_cajero_automatico,
       "ALTA_TARJETA_DEBITO": procesar_alta_tarjeta_debito
    }
    

    





