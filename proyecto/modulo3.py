from clientes import*

def registrar(clientes):
    nombre=input("ingrese su nombre o razon social:")
    id=input("ingrese su id o rif: ")
    correo=input("ingrese su correo electronico: ")
    direccion=input("ingrese su dirrecion de envio: ")
    telefono=input("ingrese su telefono: ")
    juridico=input("eres juridico?: n\n1-si\n2-no\n->")
    cliente = Clientes(nombre, id ,correo,direccion,telefono, juridico == "1")

    if juridico== "1":
        nombre_contacto=input("ingrese su nombre de contacto: ")
        telefono_contacto=input("ingrese su telefono de contacto")
        correo_contacto=input("ingrese su correo electronico de contacto: ")
        cliente.nombre_contacto = nombre_contacto
        cliente.correo_contacto=correo_contacto
        cliente.telefono_contacto=telefono_contacto

    clientes.append(cliente)


def modificar_cliente (clientes):
    id=input("ingrese el id o rif: ")
    cliente = None
    for c in clientes:
        if c.id == id:
            cliente = c
            break
    if cliente.juridico:
        informacion=input("eliga que quieres modificar:n\n1-nombre\n2-id\n3-correo\n4-direccion\telefono\n6-nombre_contacto\n7-telefono_contacto\n8-correo_contacto\n->")
    
    else:
        informacion=input("eliga que quieres modificar:n\n1-nombre\n2-id\n3-correo\n4-direccion\n5-telefono\n->")
    if informacion=="1":
        nombre=input("ingrese el nuevo nombre: ")
        cliente.nombre=nombre
    if informacion=="2":
        id=input("ingrese su nuevo id: ")
        clientes.id=id
    if informacion=="3":
        correo=input("ingrese su nuevo correo: ")
        clientes.correo=correo
    if informacion=="4":
        direccion=input("ingrese su nueva direccion: ")
        cliente.direccion=direccion
    if informacion=="5":
        telefono=input("ingrese su nuevo telefono: ")
        cliente.telefono=telefono
    if informacion=="6":
        nombre_contacto=input("ingrese su nuevo nombre de contacto: ")
        cliente.nombre_contacto=nombre
    if informacion=="7":
        telefono_contacto=input("agregue su nuevo telefono de contacto: ")
        cliente.telefono_contacto=telefono_contacto
    if informacion=="8":
        correo_contacto=input("ingrese su nuevo correo de contacto: ")
        cliente.correo_contacto=correo_contacto

def eliminar_cliente(clientes):
    id=input("ingrese la cedula o rif del cliente que desee eliminar: ")
    for c in clientes:
        if c.id==id:
            clientes.remove(c)
            print("cliente eliminado")

def buscar_cliente(clientes):
    cliente=input("elija en que funcion desea buscar: n\n1-id o rif\n2-correo electronico\n->")
    if cliente=="1":
        id=input("ingrese la cedula o rif del cliente que desee buscar: ")

        for c in clientes:
            if c.id==id:
                if c.juridico:
                    print(f"su cliente: {c.nombre}, {c.id},{c.correo},{c.direccion},{c.telefono}, {c.nombre_contacto},{c.telefono_contacto},{c.correo_contacto}")

                else:
                    print(f"su cliente: {c.nombre}, {c.id},{c.correo},{c.direccion},{c.telefono}")

    if cliente=="2":
        correo=input("ingrese el correo electronico que desee buscar: ")

        for c in clientes:
            if c.correo==correo:
                print(f"su cliente: {c.nombre}, {c.id},{c.correo},{c.direccion},{c.telefono}")


