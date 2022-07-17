from .direccion import Direccion

class Cliente:
    nombre = ""
    apellido = ""
    numero = ""
    dni = ""

    def __init__(self, datos_cliente):
        self.nombre = str(datos_cliente["nombre"])
        self.apellido = str(datos_cliente["apellido"])
        self.numero = str(datos_cliente["numero"])
        self.dni = str(datos_cliente["dni"])
        self.direccion = Direccion(datos_cliente["direccion"])

    def puede_crear_chequera(self) -> bool:
        pass
    def puede_crear_tarjeta_credito(self) -> bool:
        pass
    def puede_comprar_dolar(self) -> bool:
        pass