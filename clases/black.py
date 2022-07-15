from .cliente import Cliente

class Black(Cliente):
    def puede_crear_chequera() -> bool:
        pass    #Sólo puede crear dos...
    def puede_crear_tarjeta_credito() -> bool:
        pass    #Sólo puede crear cinco...
    def puede_comprar_dolar() -> bool:
        return True

    