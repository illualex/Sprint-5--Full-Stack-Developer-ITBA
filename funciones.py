def calcular_monto_total(precio_dolar, monto_a_adquirir, impuesto_pais, ganancias, tipo_cliente="clienteClassic"):
    tarifas = {
        "clienteClassic": {
            "impuesto_pais": 0.5,
            "ganancias": 1
        },
        "clienteGold": {
            "impuesto_pais": 0.1,
            "ganancias": 0.5
        },
        "clienteBlack": {
            "impuesto_pais": 0,
            "ganancias": 0
        }
    }

    if tipo_cliente not in tarifas:
        raise ValueError("Tipo de cliente no válido")

    impuesto_pais_cliente = tarifas[tipo_cliente]["impuesto_pais"]
    ganancias_cliente = tarifas[tipo_cliente]["ganancias"]

    monto_sin_impuestos = precio_dolar * monto_a_adquirir
    impuesto = monto_sin_impuestos * impuesto_pais_cliente / 100
    ganancia = monto_sin_impuestos * ganancias_cliente / 100
    monto_total = monto_sin_impuestos + impuesto + ganancia
    return monto_total

def descontar_comision(monto, porcentaje_comision):
    comision = monto * porcentaje_comision / 100
    monto_descontado = monto - comision
    return monto_descontado

def calcular_monto_plazo_fijo(monto, interes_porcentaje):
    monto_final = monto + (monto * interes_porcentaje / 100)
    return monto_final
