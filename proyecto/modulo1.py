from productos import *


def buscar(productos):
    tipo=input("eliga los porductos que desees ver: n\n1-categoria\n2-precio\n3-nombre\n4-inventario\n-> ")
    tipo = int(tipo)
    if tipo==1:
        categoria=input("escriba la cagetoria del producto:  ")
        encontrados = []
        for producto in productos:
            if producto.categoria == categoria:
                encontrados.append(producto)

        for encontrado in encontrados:
            print(f"nombre: {encontrado.nombre}\n descripcion:{encontrado.descripcion}\n precio:{encontrado.precio}\n  categoria:{encontrado.categoria}\n  inventario:{encontrado.inventario}\n-> ")

    if tipo==2: 
        precio=input("escribe el precio del producto: ")
        encontrados=[]
        for producto in productos:
            if producto.precio== precio:
                encontrados.append(producto)

        for encontrado in encontrados:
            print(f"nombre: {encontrado.nombre}\n descripcion:{encontrado.descripcion}\n precio:{encontrado.precio}\n  categoria:{encontrado.categoria}\n  inventario:{encontrado.inventario}\n-> ")

    if tipo==3:
        nombre=input("eliga el nombre del producto: ")
        encontrados=[]
        for producto in productos:
            if producto.nombre==nombre:
                encontrados.append(producto)
        for encontrado in encontrados:
             print(f"nombre: {encontrado.nombre}\n descripcion:{encontrado.descripcion}\n precio:{encontrado.precio}\n  categoria:{encontrado.categoria}\n  inventario:{encontrado.inventario}\n-> ")

    if tipo==4:
        
        for producto in productos:
            if producto.inventario >0:
                 print(f"nombre: {producto.nombre}\n descripcion:{producto.descripcion}\n precio:{producto.precio}\n  categoria:{producto.categoria}\n  inventario:{producto.inventario}\n-> ")

        
def agregar(productos):
    nombre=input(" agrege el nombre del producto que desee:")
    precio=input("agregue el precio del producto:")
    categoria=input("agregue la categoria que desees: ")
    inventario=input("cuantos productos hay disponibles: ")
    descripcion=input("descripcion del producto: ")
    opcional=input("deseas agregar un modelo de vehiculo?: n\n1-si\n2-no\n-> ")


    producto = Productos(nombre, descripcion, precio , categoria, int(inventario))
    if int(opcional)==1:
       modelo= input("ingrese el modelo que quieras aplicar:")
       producto.opcional = modelo
    
    productos.append(producto)
    
def modificar(productos):
    nombre = input(" agrege el nombre del producto que desee modificar: ")
    for  p in productos:
        if p.nombre == nombre:
            producto = p
    opcion=input("eliga que producto desea modoficar:n\n1-nombre\n2-precio\n3-categoria\n4-inventario\n5-descripcion\n6-opcional\n->")
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("Ingrese el nuevo nombre: ")
        producto.nombre = nombre

    if opcion==2:
        precio=input("ingrese el precio que desees modificar: ")
        producto.precio = precio 
    
    if opcion==3:
        caterogia=input("ingrese la cagetoria que desees modificar: ")
        producto.categoria = caterogia

    if opcion==4:
        inventario=input("ingrese el inventario que desees modificar: ")
        producto.inventario = inventario

    if opcion==5:
        descripcion=input("ingrese la descripcion que desees modificar: ")
        producto.descripcion = descripcion

    if opcion==6:
        opcional= input("ingrese producto opcional que desees modificar: ")
        producto.opcional = opcional

    

def eliminar(productos):

     nombre=input("ingrese el producto que desee eliminar: ")

     for p in productos:
         if p.nombre== nombre:
             productos.remove(p)
             print("Producto eliminado")



productos = []

