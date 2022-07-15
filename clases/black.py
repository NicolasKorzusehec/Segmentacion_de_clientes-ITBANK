from .cliente import Cliente
from .cuenta import Cuenta
class Black(Cliente):
    def __init__(self, datos_cliente):
        valores = [100000,-1,0,0,10000]

        super().__init__(datos_cliente)
        self.cuenta = Cuenta(valores)

    def puede_crear_chequera() -> bool:
        pass    #Sólo puede crear dos...
    def puede_crear_tarjeta_credito() -> bool:
        pass    #Sólo puede crear cinco...
    def puede_comprar_dolar() -> bool:
        return True

    