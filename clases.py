class Cliente:
    nombre = ""
    apellido = ""
    numero = ""
    dni = ""

    def puede_crear_chequera():
        pass
    def puede_crear_tarjeta_credito():
        pass
    def puede_comprar_dolar():
        pass

class Classic(Cliente):
    def puede_crear_chequera():
        return False
    def puede_crear_tarjeta_credito():
        return False
    def puede_comprar_dolar():
        return False

class Gold(Cliente):
    def puede_crear_chequera():
        pass    #Sólo puede crear una...
    def puede_crear_tarjeta_credito():
        pass    #Sólo puede crear una...
    def puede_comprar_dolar():
        return True

class Black(Cliente):
    def puede_crear_chequera():
        pass    #Sólo puede crear dos...
    def puede_crear_tarjeta_credito():
        pass    #Sólo puede crear cinco...
    def puede_comprar_dolar():
        return True

class Cuenta():
    def limite_extraccion_diario():
        pass
    def limite_transferencia_recibida():
        pass
    def monto():
        pass
    def costo_transferencias():
        pass
    def saldo_descubierto_disponible():
        pass
    
class Direccion():
    calle =""
    numero=""
    ciudad=""
    provincia=""
    pais=""

    #Validate
    #Output As Label

class Razon():
    tipo =""

    def resolver(cliente,evento):
        pass

class RazonAltaChequera(Razon):
    pass

class RazonAltaTarjetaCredito(Razon):
    pass

class RazonCompraDolar(Razon):
    pass

class RazonRetiroEfectivo(Razon):
    pass

class RazonTransferenciaEnviada(Razon):
    pass

class RazonTransferenciaRecibida(Razon):
    pass