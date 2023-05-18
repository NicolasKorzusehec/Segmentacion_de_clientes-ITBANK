from clases import Classic, Gold, Black
from razones import RazonAltaChequera,RazonAltaTarjetaCredito,RazonCompraDolar,RazonRetiroEfectivo,RazonTransferenciaEnviada,RazonTransferenciaRecibida, razon
import json, datetime, webbrowser, os

# Modificación: Es interesante plantear ciertas constantes a inicio del archivo para evitar errores de tipeo, ejemplo los tipos de transferencia. Separar alguna de las funciones de aca como otros objetos, como el de la web que se genera.


# Busca y abre un archivo JSON en modo lectura, deserializa el objeto JSON, lo convierte en un objeto Python y finalmente lo retorna.
# Si el archivo especificado no existe o no tiene formato JSON, devuelve un mensaje de error.
def leerJSON(filename):
    try:
        archivoJson = open(filename, "r", newline="")
        datos_cliente = json.load(archivoJson)
        archivoJson.close()
    except FileNotFoundError:                              
        print("Error: El archivo especificado no existe.")
        return
    except json.JSONDecodeError:
        print("Error: El archivo especificado no tiene formato JSON.")
        return
    else:
        return datos_cliente

# Crea y retorna una instancia de un objeto subclase de Cliente según el tipo especificado en el diccionario 'datos_cliente'.
def crearCliente(datos_cliente):
    if datos_cliente["tipo"] == "BLACK":
        cliente = Black(datos_cliente)
    elif datos_cliente["tipo"] == "GOLD":
        cliente = Gold(datos_cliente)
    elif datos_cliente["tipo"] == "CLASSIC":
        cliente = Classic(datos_cliente)
    else:
        print("Todavia no fue definido ese tipo de cliente.")
    return cliente

# Itera sobre un array de transacciones, controlando las que son rechazadas para asignarles la razón correspondiente según el tipo de transacción.
# Retorna un array de diccionarios de las transacciones procesadas.
def procesarTransacciones(transacciones, cliente):
    transacciones_procesadas = []   # Array de diccionarios de cada transacción.
    razon = ""
    for transaccion in transacciones:
        if transaccion["estado"] == "RECHAZADA":
            if transaccion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                razon = RazonRetiroEfectivo().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "ALTA_TARJETA_CREDITO":
                razon = RazonAltaTarjetaCredito().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "ALTA_CHEQUERA":
                razon = RazonAltaChequera().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "COMPRA_DOLAR":
                razon = RazonCompraDolar().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "TRANSFERENCIA_ENVIADA":
                razon = RazonTransferenciaEnviada().resolver(cliente, transaccion)
            elif transaccion["tipo"] == "TRANSFERENCIA_RECIBIDA":
                razon = RazonTransferenciaRecibida().resolver(cliente, transaccion)
            else:
                print("Todavia no fue definida esta transaccion.")
        else:
            razon = ""
        transacciones_procesadas.append({"fecha": transaccion["fecha"], "tipo": transaccion["tipo"], "estado":transaccion["estado"], "monto": transaccion["monto"], "razon": razon})
    return transacciones_procesadas

def aclaracionHabilitado(tipo):
    if tipo == "CLASSIC":
        return """
<ul>
    <li>Tiene solamente una tarjeta de débito que se crea junto con el cliente.</li>
    <li>Solo tiene una caja ahorro en pesos creada cuando se dio de alta el cliente.</li>
    <li>Como no tiene cuenta en dólares, no puede comprar y vender dólares.</li>
    <li>Solo se le permite retirar hasta un máximo de $10.000 diarios por cajero.</li>
    <li>No tienen acceso a tarjetas de crédito, ni chequeras.</li>
    <li>La comisión por transferencias hechas es de 1%.</li>
    <li>puede recibir transferencias mayores a $150.000 sin previo aviso.</li>
</ul>"""
    elif tipo == "GOLD":
        return """
<ul>
    <li>Tiene una tarjeta de débito que se crea con el cliente.</li>
    <li>Tiene una cuenta corriente con un descubierto de $10.000. Hay que tener presente que como tiene cuenta corriente el saldo en la cuenta podría ser negativo y hasta -$10.000 si tiene cupo diario para la operación que se quiera realizar.</li>
    <li>Tiene una caja de ahorro en dólares, por lo que puede comprar dólares.</li>
    <li>Puede tener solo una tarjeta de crédito.</li>
    <li>Las extracciones de efectivo tienen un máximo de $20.000 por día.</li>
    <li>Pueden tener una chequera.</li>
    <li>La comisión por transferencias hechas es de 0,5%.</li>
    <li>No puede recibir transferencias mayores a $500.000 sin previo aviso.</li>
</ul>"""
    elif tipo == "BLACK":
        return """
<ul>
    <li>Los clientes Black tienen una caja de ahorro en pesos, cuenta corriente en pesos, y una caja de ahorro en dólares.</li>
    <li>Pueden tener un descubierto en su cuenta corriente de hasta $10.000.</li>
    <li>Pueden tener hasta 5 tarjetas de crédito.</li>
    <li>Pueden extraer hasta $100.000 por día.</li>
    <li>Pueden tener hasta dos chequeras</li>
    <li>No se aplican comisiones a las transferencias.</li>
    <li>Pueden recibir transferencias por cualquier monto sin previa autorización.</li>
</ul>"""
    else:
        return "Tipo no definido"

# Crea el contenido de un documento HTML que contiene los datos del cliente y una tabla con los datos de las transacciones procesadas.
def contenidoHtml(cliente, transacciones_procesadas):
    listado = ""
    for transaccion in transacciones_procesadas:
        listado += f"""
        <tr>
            <td>{transaccion["fecha"]}</td>
            <td>{transaccion["tipo"]}</td>
            <td>{transaccion["estado"]}</td>
            <td>{transaccion["monto"]}</td>
            <td>{transaccion["razon"]}</td>
        </tr>
        """
    aclaracion = aclaracionHabilitado(cliente.tipoDeCliente)
    contenido = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <title>Listado de Transacciones</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" />
    </head>
    <body class="container align-items-center justify-content-center">
        <header class="col">
            <h1 class="row mt-3">Listado de Transacciones</h1>
        </header>
        <section  id="datosCliente">
            <div class="row">
                <hr>
                <p>Nombre: {cliente.nombre} {cliente.apellido}</p>
                <hr>
                <p>Número de cliente: {cliente.numero}</p>
                <hr>
                <p>Documento: {cliente.dni}</p>
                <hr>
                <p>Dirección: {str(cliente.direccion)}</p>
                <hr>
                <details class="mb-3">
                    <summary>Tipo de cliente: {cliente.tipoDeCliente}</summary>
                    <p>{aclaracion}</p>
                </details">
                <hr>
            </div>
        </section>
        <section id="tabla">
            <table class="table">
                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Tipo</th>
                        <th>Estado</th>
                        <th>Monto</th>
                        <th>Razón</th>
                    </tr>
                </thead> 
                <tbody>
                    {listado}
                </tbody>    
            </table>
        </section>
    </body>
    </html>
    """
    return contenido

# Genera un documento HTML, inserta los datos del cliente y las transacciones, y lo intenta abrir en el navegador.
def generarHtml(cliente, transacciones_procesadas):
    contenido = contenidoHtml(cliente, transacciones_procesadas)
    timestamp = int(datetime.datetime.now().timestamp())
    documento_html = f"index-{timestamp}.html"
    ruta_html = os.path.join("resultados", documento_html)

    with open(ruta_html, "w", encoding="utf-8", newline="") as salida:   
        salida.write(contenido)
    try:
        webbrowser.open(ruta_html)
    except FileNotFoundError:
        print("No se ha podido generar la salida")

if __name__ == "__main__":
    archivo = "eventos\eventos_classic.json"  # definir valor como constantes o que se muestre los archivos de la carpeta eventos.
    datos_cliente = leerJSON(archivo)
    if not datos_cliente == None:                   # Datos cliente = Diccionario leído del JSON
        cliente = crearCliente(datos_cliente)       # cliente = Objeto del cliente
        transacciones_procesadas = procesarTransacciones(datos_cliente["transacciones"], cliente)   # Array con las transacciones procesadas
        generarHtml(cliente, transacciones_procesadas)
