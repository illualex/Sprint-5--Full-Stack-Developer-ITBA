from resumen import Resumen

#Cliente Padre con las variables de "CLASSIC", "GOLD", "BLACK" en 0 para después pisarlas
# según cada Tipo de Cliente y sus Requerimientos.
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
        self.cantidad_extensiones = 0
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

    # Función para calcular el monto.
    def calcular_monto_total(self, transaccion):
        impuesto_pais = 0.30  # Impuesto país del 30%
        ganancias = 0.35  # Ganancias del 35%
        total = transaccion["monto"] * self.PRECIO_DOLAR
        total += total * impuesto_pais
        total += total * ganancias
        return total
    
    # Función para descontar comisión.
    def descontar_comision(self, monto, comision_porcentaje):
        comision = monto * comision_porcentaje
        return monto - comision

    #Función para calcular plazo fijo.
    def calcular_monto_plazo_fijo(self, monto, interes):
        if interes < 0:
            return "Operación rechazada: El interés no puede ser negativo"
        else:
            monto_final = monto * (1 + (interes / 100))
            return monto_final
    
    #Función para Agregar tarjetas de Débito/Crédito. + Agregar cuenta para Pesos o Dólares.
    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)
    def agregar_tarjeta_debito(self, tarjeta):
        self.tarjetas_debito.append(tarjeta)
    def agregar_tarjeta_credito(self, tarjeta):
        self.tarjetas_credito.append(tarjeta)
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    # SWITCH de Funciones según el requerimiento de cada Tipo de Cliente.
    # Según el tipo de función se uso a nivel Padre (No repetir código) y otras son dependiendo del requerimiento de los Hijos.
    def procesar_retiro_efectivo_cajero_automatico(self, transaccion):
        if transaccion["saldoDisponibleEnCuenta"] < transaccion["monto"] or transaccion["monto"] > self.limite_retiro_diario:
            return "El cliente no dispone de saldo suficiente para retirar en cajero."
    def procesar_retiro_efectivo_por_caja(self, transaccion):
        if transaccion["monto"] > transaccion["saldoDisponibleEnCuenta"]:
            return "El cliente no posee el saldo suficiente para realizar el retiro."
    def procesar_compra_tarjeta_credito(self, transaccion):
        pass
    def procesar_alta_tarjeta_credito(self, transaccion):
        pass
    def procesar_alta_tarjeta_debito(self, transaccion):
        if transaccion["cantTarjetasDisponibles"] == 0:
            return "No puede dar de alta la tarjeta de debito, no tiene disponible."
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
    def procesar_alta_plazo_fijo(self, transaccion):
       if transaccion["monto"] > transaccion["saldoDisponibleEnCuenta"]:
           return "El cliente no posee saldo suficiente para realizar la operación de Plazo fijo."
       if transaccion["interesPlazoFijo"] < 0:
           return "No se puede realizar operación de Plazo fijo con interés negativo."
    
    # Función para procesar y buscar el tipo de transaccion dentro del Switch según el tipo dado.
    def procesar_transaccion(self):
        resumen_completo = []

        # Aplica las restricciones especificas en cada Tipo de Cliente ("CLASSIC", "GOLD", "BLACK"),
        # con sus requerimientos propios de cada Tipo de Transacción con su función en caso de "RECHAZADA".
        for transaccion in self.transacciones:
            if transaccion["estado"] == "RECHAZADA":
                funcion = self.switch.get(transaccion.get("tipo"))
                if funcion is None:
                    funcion = Cliente.switch.get(transaccion.get("tipo"))
                
                if funcion:
                    # Se toma el "motivo" de rechazo y se carga en una variable para la salida en HTML.
                    motivo = funcion(self, transaccion)
                    resumen = Resumen(transaccion["estado"], transaccion["tipo"], transaccion["fecha"], transaccion["numero"], motivo)
                    resumen_completo.append(resumen)
                else:    
                    print(f"Operación no reconocida: {transaccion.get('tipo')}")
            else:
                # Si el estado es "ACEPTADA", ingresa directo a la salida. 
                resumen = Resumen(transaccion["estado"], transaccion["tipo"], transaccion["fecha"], transaccion["numero"], "Operación aceptada.")
                resumen_completo.append(resumen)

        # Se retorna una lista con el resumen de todas las transacciones.
        return resumen_completo

    # Funciones del Padre.
    switch = {
       "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": procesar_retiro_efectivo_cajero_automatico,
       "RETIRO_EFECTIVO_POR_CAJA": procesar_retiro_efectivo_por_caja,
       "ALTA_TARJETA_DEBITO": procesar_alta_tarjeta_debito,
       "ALTA_PLAZO_FIJO": procesar_alta_plazo_fijo
    }
    

    





