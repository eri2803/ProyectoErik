from ventas import*
est_ventas = {}
est_productos = {}
est_clientes = {}
def registro (ventas, productos, clientes):
    nombre=input("ingrese el nombre del cliente: ")
    for cliente in clientes:
        if cliente.nombre==nombre:
            nombre = cliente
            if cliente in est_clientes.keys():
                est_clientes[cliente] += 1
            else:
                est_clientes[cliente] = 1


    carrito = {}

    fecha=input("ingrese la fecha: ")
    indice = 1
    for p in productos: 
        print(f"{indice} - {p.nombre} - {p.precio}")
        indice+=1
    while True:
        a = input("Ingrese el indice del producto: ")
        cantidad= int(input("ingrese la cantidad de producto: "))
        carrito[productos[int(a) -1]] = cantidad

        if productos[int(a) -1] in est_productos.keys():
            est_productos[productos[int(a) -1]] += cantidad

        else:
            est_productos[productos[int(a) -1]] = cantidad

        salir = input("Desea salir? 1 SI 2 NO ")
        if int(salir) == 1:
            break

    
    pago=input("ingrese metodo pago: n\n1-decontado \n2- divisa\n->")
    descuento = 0
    igtf = 0
    if pago =="1":
        descuento=0.05
    if pago =="2":
        igtf = 0.03
    iva=0.16
    subtotal = 0
    for i, j in carrito.items():
        subtotal += int(i.precio) * j
    envio=input("eliga el metodo de envio:")
    print(f"el subtotal es:{subtotal}")
    print(f" el descuento es: {descuento*subtotal}")
    print(f"el IVA es: {iva*subtotal}")
    print(f"en divisa seria: {igtf*subtotal}")
    print(f"el total seria:{subtotal - subtotal*descuento+subtotal*iva+subtotal*igtf}")

    venta=Ventas(nombre, carrito,pago,envio,fecha, subtotal - subtotal*descuento+subtotal*iva+subtotal*igtf)
    ventas.append(venta)

def generar_factura(ventas):
    cedula=input("ingrese su cedula: ")
    indice = 1
    facturas = []
    for venta in ventas:
        if venta.cliente.id== cedula:
            print(indice)
            facturas.append(venta)
            venta.mostrar()
            indice +=1
    venta=input("eliga el indice de la venta que desees visualizar: ")
    facturas[venta-1].factura()
    if facturas[venta-1].cliente.juridico:
        credito=input("eliga su plazo de compras con credito: n\n1-15 dias n\n2-30 dias n\n-> ")
        

def buscar_venta(ventas):
    opcion=input("ingrese la opcion: n\n1-cliente\n2-fecha\n->")
    if opcion=="1":
        usario=input("ingrese la id del usuario: ")
        for venta in ventas:
          if  venta.cliente.id== usario:
              print(f"nombre del cliente:{venta.cliente.nombre}") 
              print(f"el producto es: {venta.producto}")
              print(f"el monto es: {venta.total}")
              print(f"el envio es: {venta.envio}")
              print(f"el metodo de pago es:{venta.pago}")
              print(f"la fecha es : {venta.fecha}")

    if opcion =="2":
        fecha=input("ingrese la fecha: ")
        for venta in ventas:
          if  venta.fecha== fecha:
              print(f"nombre del cliente:{venta.cliente.nombre}") 
              print(f"el porducto es: {venta.producto}")
              print(f"el monto es: {venta.total}")
              print(f"el envio es: {venta.envio}")
              print(f"el metodo de pago es:{venta.pago}")
              print(f"la fecha es : {venta.fecha}")


    