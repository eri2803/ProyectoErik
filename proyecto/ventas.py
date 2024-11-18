class Ventas:
    def __init__(self,cliente,productos,pago,envio,fecha,total):
        self.cliente=cliente
        self.productos=productos
        self.pago=pago
        self.envio=envio
        self.fecha= fecha
        self.total=total
    
    def mostrar(self):
        print(f"ventas: {self.fecha},{self.total}")
    
    def facuras(self):
        print(f"ventas: {self.cliente.nombre},{self.pago},{self.envio},{self.fecha},{self.total}")
        for p, c in self.productos.items():
            print(f"{p.nombre} : {c} unidades.")