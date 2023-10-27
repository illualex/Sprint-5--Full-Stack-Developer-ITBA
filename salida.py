# Genera un HTML de salida.
# Utiliza los Datos del Cliente para saber de quien es la operación y Genera un Resumen de su cuenta.
class Salida:
    def generar_tabla_html(cliente, resumen):
        with open('informe.html', 'w') as archivo:
            # Escribe la estructura básica del HTML
            archivo.write('<html>')
            archivo.write('<head>')
            archivo.write('<title>Informe</title>')
            archivo.write('</head>')
            archivo.write('<body>')
            
            # Crea la tabla de datos del cliente
            archivo.write('<h2>Datos del Cliente</h2>')
            archivo.write('<table border="1">')
            archivo.write('<tr><th>Número</th><th>Nombre</th><th>Apellido</th><th>DNI</th><th>Tipo</th></tr>')
            archivo.write(f'<tr><td>{cliente.numero}</td><td>{cliente.nombre}</td><td>{cliente.apellido}</td><td>{cliente.dni}</td><td>{cliente.tipo}</td></tr>')
            archivo.write('</table>')
            
            # Crea la tabla de resumen
            archivo.write('<h2>Resumen</h2>')
            archivo.write('<table border="1">')
            archivo.write('<tr><th>Número</th><th>Estado</th><th>Tipo</th><th>Fecha</th><th>Motivo</th></tr>')
            for r in resumen:
                archivo.write(f'<tr><td>{r.numero}</td><td>{r.estado}</td><td>{r.tipo}</td><td>{r.fecha}</td><td>{r.motivo}</td></tr>')
            archivo.write('</table>')
            
            # Cierra el cuerpo y el HTML
            archivo.write('</body>')
            archivo.write('</html')

        # Mensaje de confirmación de la salida de archivo en HTML.
        print("Archivo HTML 'informe.html' creado con éxito.")