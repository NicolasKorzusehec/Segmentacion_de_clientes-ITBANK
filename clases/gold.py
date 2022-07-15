from .cliente import Cliente

class Gold(Cliente):
    def puede_crear_chequera() -> bool:
        pass    #Sólo puede crear una...
    def puede_crear_tarjeta_credito() -> bool:
        pass    #Sólo puede crear una...
    def puede_comprar_dolar() -> bool:
        return True