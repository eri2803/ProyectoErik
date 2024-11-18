class Pago:
    def __init__(self,cliente,monto, moneda,tipo_pago,fecha_pago, venta):
        self.cliente=cliente
        self.monto=monto
        self.tipo_pago=tipo_pago
        self.fecha_pago=fecha_pago
        self.moneda=moneda 
        self.venta = venta


