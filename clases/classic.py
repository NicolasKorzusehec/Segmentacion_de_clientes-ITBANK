from .cliente import Cliente
from .cuenta import Cuenta
class Classic(Cliente):

    def __init__(self, datos_cliente):
        valores = [10000,150000,0,0.01,0]

        super().__init__(datos_cliente)
        self.cuenta = Cuenta(valores)

    def puede_crear_chequera() -> bool:
        return False
    def puede_crear_tarjeta_credito() -> bool:
        return False
    def puede_comprar_dolar() -> bool:
        return False

