from .cliente import Cliente

class Classic(Cliente):
    def puede_crear_chequera() -> bool:
        return False
    def puede_crear_tarjeta_credito() -> bool:
        return False
    def puede_comprar_dolar() -> bool:
        return False

