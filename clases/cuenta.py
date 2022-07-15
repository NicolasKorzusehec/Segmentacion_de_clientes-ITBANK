class Cuenta():
    limite_extraccion_diario = 0
    limite_transferencia_recibida = 0
    monto = 0
    costo_transferencias = 0
    saldo_descubierto_disponible = 0

    def __init__(self,valores) -> None:
        self.limite_extraccion_diario = valores[0]
        self.limite_transferencia_recibida = valores[1]
        self.monto = valores[2]
        self.costo_transferencias = valores[3]
        self.saldo_descubierto_disponible = valores[4]
        