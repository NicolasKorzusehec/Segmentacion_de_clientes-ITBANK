from .direccion import Direccion
from .cuenta import Cuenta

class Cliente:
    nombre = ""
    apellido = ""
    numero = ""
    dni = ""

    def __init__(self, datos_cliente):
        self.nombre = datos_cliente["nombre"]
        self.apellido = datos_cliente["apellido"]
        self.numero = datos_cliente["numero"]
        self.dni = datos_cliente["dni"]
        self.direccion = Direccion(datos_cliente["direccion"])
        # self.cuenta = Cuenta()

    def puede_crear_chequera() -> bool:
        pass
    def puede_crear_tarjeta_credito() -> bool:
        pass
    def puede_comprar_dolar() -> bool:
        pass