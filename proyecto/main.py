from modulo1 import*
from modulo2 import*
from modulo3 import*
from modulo4 import*
from modulo5 import*
from indicadores import *

def main():
    productos = []
    ventas = []
    clientes = []
    pagos = []
    envios = []

    while True:
        opcion = input("eliga la opcion que desees: \n1-gestion de productos \n2-gestion de ventas \n3-gestion de clientes \n4-gestion de pagos \n5-gestion de envios \n6-indicadores de gestion \n7-salir \n-> ")
        if opcion == '1':
            opcion2 = input("eliga que opcion quieres realizar: \n1-agregar \n2-buscar \n3-modificar \n4-eliminar \n5-salir \n->")
            if opcion2 == '1':
                try:
                    agregar(productos)
                except:
                    print("Dato erroneo")

                
            if opcion2 == '2':
                try:
                    buscar(productos)
                except:
                    print("Dato erroneo")
            if opcion2 =='3':
                try:
                    modificar(productos)
                except:
                    print("dato erroneo")
            if opcion2 =='4':
                try:
                    eliminar(productos)
                except:
                    print("dato erroneo")
            if opcion2 =='5':
                break
        if opcion == '2':
            opcion2= input("eliga la opcion que desee ver: \n1-registrar ventas \n2-generar facutra \n3-buscar venta \n4-salir \n->")
            if opcion2=='1':
                try:
                    registro(ventas, productos, clientes)
                except:
                    print("dato erroneo")
            if opcion2=='2':
                try:
                    generar_factura(ventas)
                except:
                    print("dato erroneo")
            if opcion2=='3':
                try:
                    buscar_venta(ventas)
                except:
                    print("dato erroneo")
            if opcion2=='4':
                break
        if opcion== '3':
            opcion2=input("eliga la opcion que desee: \n1-registrar clientes \n2-modificar informacion \n3-eliminar clientes \n4-buscar clientes \n5-salir \n->")
            if opcion2=='1':
                try:
                    registrar(clientes)
                except:
                    print("dato erroneo")
            if opcion2== '2':
                try:
                    modificar_cliente(clientes)
                except:
                    print("dato erroneo")
            if opcion2== '3':
                try:
                    eliminar_cliente(clientes)
                except:
                    print("dato erroneo")
            if opcion2== '4':
                try:
                    buscar_cliente(clientes)
                except:
                    print("dato erroneo")
            if opcion2=='5':
                break
        if opcion=='4':
            opcion2=input("ingrese que opcion quieres ver; \n1-registrar pagos \n2-buscar pagos \n3-salir \n->")
            if opcion2=='1':
                try:
                    registrar_pago(pagos, clientes, ventas)
                except:
                    print("dato erroneo")
            if opcion2=='2':
                try:
                    buscar_pago(pagos)
                except:
                    print("dato erroneo")
            if opcion2=='3':
                break

        if opcion=='5':
            opcion2=input("ingrese la opcion que desea ver: \n1-registrar envios \n2-buscar envios \n3-salir \n->")
            if opcion2=='1':
                try:
                    registrar_envio(envios,pagos)
                except:
                    print("dato erroneo")
            if opcion2=='2':
                try:
                    buscar_envio(envios)
                except:
                    print("dato erroneo")
            if opcion2=='3':
                break

        if opcion == '6':
            opcion2=input("eliga la opcion: \n1- informe de ventas \n2-informes de pagos \n3-informe de envios \n4-salir")
            if opcion2== '1':
                opcion3=input("eliga cual opcion desea: \n1- ventas totales \n2-productos mas vendidos \n3-clientes mas frecuentes \n4-salir \n-> ")
                if opcion3 == "1":
                    pass
                if opcion3 == "2":
                    mas_vendidos = []
                    for x in range(5):
                        c = 0 
                        mv = None
                        for producto, valor in est_productos.items():
                            if producto not in mas_vendidos and c < valor:
                                mv = producto
                                c = valor
                        if mv != None:
                            mas_vendidos.append(mv)
                            print(f"nombre: {mv.nombre}\n descripcion:{mv.descripcion}\n precio:{mv.precio}\n  categoria:{mv.categoria}\n  inventario:{mv.inventario}\n ----------------")
                if opcion3=='3':
                    mas_frecuentes = []
                    for x in range(5):
                        c = 0 
                        mf = None
                        for cliente, valor in est_clientes.items():
                            if cliente not in mas_frecuentes and c < valor:
                                mf = cliente
                                c = valor
                        if mf != None:
                            mas_frecuentes.append(mf)
                            print(f"nombre: {mf.nombre}\n-> ")

            if opcion2=='2':
               opcion3=input("ingrese la opcion que desee: \n1-pagos totales \n2-clientes con pagos pendientes \n3-salir \n->")
               if opcion3=='1':
                   pass
               if opcion3=='2':
                    try:
                     i = Indicadores()
                     i.pendientes(pagos, ventas)
                    except:
                        pass
               if opcion3=='3':
                   break
            if opcion2=='3':
                opcion3=input("eliga la opcion que desee revisar: \n1-envios totales \n2-productos mas enviados \n3-cliente con envios pedientes \n4-salir \n->")
                
                if opcion3=='1':
                    pass 
                if opcion3=='2':
                    try:
                        mas_Enviados = []
                        for x in range(5):
                            c = 0 
                            mv = None
                            for producto, valor in productos_enviados.items():
                                if producto not in mas_Enviados and c < valor:
                                    mv = producto
                                    c = valor
                            if mv != None:
                                mas_Enviados.append(mv)
                                print(f"nombre: {mv.nombre}\n descripcion:{mv.descripcion}\n precio:{mv.precio}\n  categoria:{mv.categoria}\n  inventario:{mv.inventario}\n-> ")
                    except:
                        pass
                if opcion3=='3':
                    try:
                      i = Indicadores()
                      i.envios_pend(pagos)
                    except:
                        pass
                if opcion3=='4':
                    break
                 
                        
main()