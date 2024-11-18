from pagos import*
from clientes import *
def registrar_pago(pagos,clientes, ventas):
    cliente=input("ingrese su nombre: ")
    for c in clientes:
        if c.nombre==cliente:
            cliente = c
            break
    for venta in ventas:
        if venta.cliente == cliente:
            venta.mostrar()
    v = input("Ingrese la fecha de la venta que desea pagar: ")

    for venta in ventas:
        if venta.cliente == cliente and venta.fecha == v:
            v = venta

    if type(v) == str:
        print("Venta no encontrada")
        return
    monto=input("agregue el monto del pago: ")

    moneda=input("ingrese su  moneda de pago: ")

    tipo=input("eliga su metodo de pago: \n1-punto de venta \n2-pago movil \n3-transferencia \n4-zelle \n5-PayPal \n6-efectivo \n->")
    if tipo == "1":
        tipo = "punto de venta"
    elif tipo == "2":
        tipo = "pago movil"
    elif tipo == "3":
        tipo = "transferencia"
    elif tipo == "4":
        tipo = "zelle"
    elif tipo == "5":
        tipo = "PayPal"
    elif tipo == "6":
        tipo = "efectivo"

    fecha=input("ingrese la fecha del pago: ")

    pago = Pago(cliente, monto,moneda,tipo,fecha, v)

    pagos.append(pago)


def buscar_pago(pagos):
    usuario=input("elige en que filtro vas a buscar el pago: \n1-cliente \n2-fecha \n3- tipo de pago \n4-moneda de pago \n-> ")

    if usuario== "1":
        cliente=input("ingrese el nombre del cliente: ")
        for pago in pagos:
            if pago.cliente.nombre == cliente:
               print(f"su cliente es: {pago.moneda},\nMonto: {pago.monto}, \nTipo: {pago.tipo_pago},\nFecha:{pago.fecha_pago},\nMoneda:{pago.moneda} ")

    if usuario=="2":
        fecha=input("ingrese la fecha del cliente: ")
        for pago in pagos:
            if pago.fecha_pago==fecha:
               print(f"su cliente es: {pago.moneda},\nMonto: {pago.monto}, \nTipo: {pago.tipo_pago},\nFecha:{pago.fecha_pago},\nMoneda:{pago.moneda} ")
    if usuario== "3":
        tipo=input(f"ingrese el tipo de pago del cliente: ")
        for pago in pagos:
            if pago.tipo_pago==tipo:
                print(f"su cliente es: {pago.moneda},\nMonto: {pago.monto}, \nTipo: {pago.tipo_pago},\nFecha:{pago.fecha_pago},\nMoneda:{pago.moneda} ")

    if usuario=="4":
        moneda=input("ingrese la moneda de su cliente: ")
        for pago in pagos:
            if pago.moneda==moneda:
               print(f"su cliente es: {pago.moneda},\nMonto: {pago.monto}, \nTipo: {pago.tipo_pago},\nFecha:{pago.fecha_pago},\nMoneda:{pago.moneda} ")



