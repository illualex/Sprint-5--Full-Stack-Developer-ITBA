import argparse
import json
from cliente import Cliente
from clienteClassic import ClienteClassic
from clienteGold import ClienteGold
from clienteBlack import ClienteBlack
from resumen import Resumen
from salida import Salida

#Leer archivo Json. + Verificar si el archivo existe.
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

#Cargar el contenido del archivo para poder ser procesado luego. + Verificar si están todos los campos requeridos.
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
                transacciones_obj.append({
                    "estado": transaccion.get("estado"),
                    "tipo": transaccion.get("tipo"),
                    "cuentaNumero": transaccion.get("cuentaNumero"),
                    "permitidoActualParaTransaccion": transaccion.get("permitidoActualParaTransaccion"),
                    "saldoDisponibleEnCuenta": transaccion.get("saldoDisponibleEnCuenta"),
                    "cantTarjetasDisponibles": transaccion.get("cantTarjetasDisponibles"),
                    "cantChequerasDisponibles": transaccion.get("cantChequerasDisponibles"),
                    "cantCuentasDisponibles": transaccion.get("cantCuentasDisponibles"),
                    "interesPlazoFijo": transaccion.get("interesPlazoFijo"),
                    "monto": transaccion.get("monto"),
                    "fecha": transaccion.get("fecha"),
                    "numero": transaccion.get("numero")
                })
            cliente = Cliente(numero, nombre, apellido, dni, tipo, transacciones_obj)
            return cliente
        else:
            print("El contenido del JSON no tiene todos los campos esperados.")
    else:
        print("El contenido del JSON es nulo.")
    
#Clasificar según el Tipo de Cliente.
def procesar_archivo(cliente):
    resumen = []
    if cliente.tipo == "CLASSIC":
        cliente_instancia = ClienteClassic(cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo, cliente.transacciones)
    elif cliente.tipo == "GOLD":
        cliente_instancia = ClienteGold(cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo, cliente.transacciones)
    elif cliente.tipo == "BLACK":
        cliente_instancia = ClienteBlack(cliente.numero, cliente.nombre, cliente.apellido, cliente.dni, cliente.tipo, cliente.transacciones)
    else:
        #Si se ingresa un tipo de cliente distinto a los que se espera.
        return []
    
    resumen = cliente_instancia.procesar_transaccion()
    return resumen

#Leer el archivo y procesarlo usando argparse. + Salida HTML.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Nombre del archivo JSON a cargar")
    args = parser.parse_args()
    archivo = args.archivo
    contenido = cargar_archivo_json(archivo)
    cliente = leer_archivo_json(contenido)
    
    if cliente:
        resumen = procesar_archivo(cliente)

        # Llamar a la función para generar el informe HTML de salida.
        Salida.generar_tabla_html(cliente, resumen)