from clases import Classic, Gold, Black
import json, datetime, webbrowser

def leerJSON():
    try:
        archivoJson = open("eventos\eventos_classic.json", "r", newline="")
    except FileNotFoundError:                              
        print("Error. El archivo especificado no existe.")
    else:
        datos_cliente = json.load(archivoJson)
        return datos_cliente
        
def crearCliente(datos_cliente):
    if datos_cliente["tipo"] == "CLASSIC":
        cliente = Classic(datos_cliente)
    elif datos_cliente["tipo"] == "GOLD":
        cliente = Gold(datos_cliente)
    elif datos_cliente["tipo"] == "BLACK":
        cliente = Black(datos_cliente)

    return cliente

def procesarTransacciones(transacciones):
    for transaccion in transacciones:
        if transaccion["estado"] == "RECHAZADA":
            pass

def generarHtml(cliente):
    timestamp = int(datetime.datetime.now().timestamp())
    documento_html = f"index-{timestamp}.html"

    with open(documento_html, "w", newline="") as salida:   
        pass #Escribir contenido del html

    try:
        webbrowser.open(documento_html)
    except FileNotFoundError:
        print("No se ha podido generar la salida")

if __name__ == "__main__":
    datos_cliente = {}
    datos_cliente = leerJSON()
    cliente = crearCliente(datos_cliente)
    procesarTransacciones(datos_cliente["transacciones"])
    generarHtml(cliente)
    
