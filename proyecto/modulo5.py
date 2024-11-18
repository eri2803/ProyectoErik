from envios import*
from pagos import*
from clientes import*

productos_enviados = {}
def registrar_envio(envios, pagos):
    cedula=input("ingrese su cedula:  ")
    fecha=input("ingrese la fecha de pago: ")
    pago = None
    for p in pagos:
        if p.cliente.id == cedula and p.fecha_pago == fecha:
            pago = p
            break
    if pago == None:
        print("Pago no encontrado")
        return
    servicio=input("eliga el metodo de envio: \n1-zoom \n2-delivery ")
    if servicio=="1":
        servicio="zoom"
    if servicio =="2":
        servicio="delivery"
        nombre_delivery=input("ingrese el nombre del motorizado: ")
        cedula_delivery=input("ingrese la cedula del motorizado: ")
        telefono_delivery=input("ingrese el telefono del motorizado: ")
        
    costo=input("ingrese su costo del envio: ")
    for producto, cant in pago.venta.productos.items():
        if producto in productos_enviados.keys():
            productos_enviados[producto] += cant
        else:
            productos_enviados[producto] = cant

    envio=Envio(pago, servicio,costo) 
    try:
        envio.nombre_delivery = nombre_delivery
        envio.cedula_delivery = cedula_delivery
        envio.telefono_delivery= telefono_delivery
    except:
        pass

    
    envios.append(envio) 

def buscar_envio(envios):
    busqueda=input("ingrese la opcion de busqueda: \n1-cliente \n2-fecha ")
    if busqueda=="1":
        cliente=input("agregue la cedula del cliente: ")
        for envio in envios:
            if envio.compra.cliente.id == cliente:
                if envio.servicio=="delivery":
                    print(f"el envio es: {envio.compra.cliente.nombre},{envio.compra.fecha_pago},{envio.servicio},{envio.nombre_delivery},{envio.cedula_delivery},{envio.telefono_delivery}")
                else:
                    print(f"el envio es: {envio.compra.cliente.nombre},{envio.compra.fecha_pago},{envio.servicio}")

    if busqueda=="2":
        fecha=input("ingrese la fecha de envio del cliente: ")
        for envio in envios:
            if envio.compra.fecha_pago==fecha:
                if envio.servicio=="delivery":
                    print(f"el envio es: {envio.compra.cliente.nombre},{envio.compra.fecha_pago},{envio.servicio},{envio.nombre_delivery},{envio.cedula_delivery},{envio.telefono_delivery}")
                else:
                    print(f"el envio es: {envio.compra.cliente.nombre},{envio.compra.fecha_pago},{envio.servicio}")
