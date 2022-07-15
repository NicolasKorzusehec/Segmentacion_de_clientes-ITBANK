from .cliente import Cliente
from .cuenta import Cuenta
class Gold(Cliente):
    def __init__(self, datos_cliente):
        valores = [20000,500000,0,0.05,10000]

        super().__init__(datos_cliente)
        self.cuenta = Cuenta(valores)

    def puede_crear_chequera() -> bool:
        pass    #Sólo puede crear una...
    def puede_crear_tarjeta_credito() -> bool:
        pass    #Sólo puede crear una...
    def puede_comprar_dolar() -> bool:
        return True