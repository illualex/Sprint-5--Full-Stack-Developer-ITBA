def calcular_monto_total(precio_dolar, monto):
    impuesto_pais = 30 # Impuesto país del 30%
    ganancias = 35  # Ganancias del 35%
   
    monto_impuesto_pais= (impuesto_pais /100) * monto
    monto_ganancias=(ganancias /100) * monto
    monto_porcentajes= monto +monto_impuesto_pais + monto_ganancias
    monto_final =monto_porcentajes /precio_dolar
    return round(monto_final ,2)
   

def descontar_comision(monto, comision):
    comision = float(comision) / 100.0
    monto_descontado = monto - (monto * comision)
    return monto_descontado

def calcular_monto_plazo_fijo(monto, interes):
    interes = float(interes) / 100.0
    monto_final = monto + (monto * interes)
    return monto_final
