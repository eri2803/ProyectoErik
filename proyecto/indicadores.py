class Indicadores:
    def __init__(self):
        pass

    def pendientes(self, pagos, ventas):
        pendientes = []
        for venta in ventas:
            encontrado = False
            for pago in pagos:
                if pago.monto == venta.total and venta.cliente == pago.cliente:
                    encontrado = True
            if not encontrado:
                pendientes.append(venta)
        
        for venta in pendientes:
            print(f"Pago Pendiente: {venta.cliente.nombre}, {venta.total}, {venta.fecha}")
        
    def envios_pend(envios, pagos):
        pendientes = []
        for pago in pagos:
            for envio in envios:
                if envio.pago == pago:
                    encontrado = True
            if not encontrado:
                pendientes.append(pago)
        for pago in pendientes:
            print(f"Envio Pendiente: {pago.cliente.nombre}, {pago.monto}, {pago.fecha_pago}")


    
        