import argparse
import json

from cliente import Cliente
from clienteClassic import ClienteClassic
from clienteGold import ClienteGold
from clienteBlack import ClienteBlack
from resumen import Resumen
from salida import Salida

def cargar_archivo_json(archivo):
    try:
        with open(archivo, 'r') as file:
            contenido = json.load(file)
        return contenido
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"El archivo '{archivo}' no es un archivo JSON válido.")
        return None

def leer_archivo_json(contenido):
    if contenido is not None:
        numero = contenido.get("numero")
        nombre = contenido.get("nombre")
        apellido = contenido.get("apellido")
        dni = contenido.get("dni")
        tipo = contenido.get("tipo")
        transacciones = contenido.get("transacciones")

        if numero is not None and nombre is not None and apellido is not None and dni is not None and tipo is not None and transacciones is not None:
            transacciones_obj = []
            for transaccion in transacciones:
                estado = transaccion.get("estado")
                tipo_transaccion = transaccion.get("tipo")
                cuenta_numero = transaccion.get("cuentaNumero")
                permitido_actual = transaccion.get("permitidoActualParaTransaccion")
                monto = transaccion.get("monto")
                fecha = transaccion.get("fecha")
                numero_transaccion = transaccion.get("numero")
                transacciones_obj.append({
                    "estado": estado,
                    "tipo": tipo_transaccion,
                    "cuentaNumero": cuenta_numero,
                    "permitidoActualParaTransaccion": permitido_actual,
                    "monto": monto,
                    "fecha": fecha,
                    "numero": numero_transaccion
                })

            cliente = Cliente(numero, nombre, apellido, dni, tipo, transacciones_obj)
            return cliente

        else:
            print("El contenido del JSON no tiene todos los campos esperados.")
    else:
        print("El contenido del JSON es nulo.")
    

def procesar_archivo(cliente):
    resumen = []
    if cliente.tipo == "CLASSIC":
        cliente_instancia = ClienteClassic(cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo, cliente.transacciones)
    elif cliente.tipo == "GOLD":
        cliente_instancia = ClienteGold(cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo, cliente.transacciones)
    elif cliente.tipo == "BLACK":
        cliente_instancia = ClienteBlack(cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo, cliente.transacciones)
    else:
        # Tipo de cliente desconocido
        return []
    
    
    resumen_completo = []
    
    """for transaccion in self.transacciones:
            if transaccion["estado"] == "RECHAZADA":
                tipo_transaccion = transaccion.get("tipo")
                
                # Verifica si la función existe en la instancia actual
                if hasattr(self, tipo_transaccion):
                    funcion = getattr(self, tipo_transaccion)
                    motivo = funcion(transaccion)
                    resumen = Resumen(transaccion["estado"], tipo_transaccion, transaccion["fecha"], transaccion["numero"], motivo)
                    resumen_completo.append(resumen)
                else:
                    print(f"Operación no reconocida: {tipo_transaccion}")
            else:
                resumen = Resumen(transaccion["estado"], transaccion["tipo"], transaccion["fecha"], transaccion["numero"], "Operación aceptada.")
                resumen_completo.append(resumen)"""

        
    
    resumen = cliente_instancia.procesar_transaccion()
    return resumen


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Nombre del archivo JSON a cargar")

    args = parser.parse_args()
    archivo = args.archivo

    contenido = cargar_archivo_json(archivo)
    cliente = leer_archivo_json(contenido)
    
    if cliente:
        resumen = procesar_archivo(cliente)
        # Llamar a la función para generar el informe HTML
        Salida.generar_tabla_html(cliente, resumen)