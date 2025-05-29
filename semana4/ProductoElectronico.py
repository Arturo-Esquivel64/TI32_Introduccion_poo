class ProductoElectronico:
    nombre:str
    precio:float
    marca:str
    mesesGarantia=int

    def __init__(self,nombre:str,precio:float, marca:str)-> None:
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.mesesGarantia = 12

    def cambiarGarantia(self, meses)-> None:
        self.mesesGarantia = meses
    
    def precioDescuento(self, porcentaje)-> None:
        descuento =self.precio * porcentaje / 100
        self.precio = self.precio - descuento
        print(f"EL descuento fue de: {descuento}")

    def detalles(self)-> None:
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Garantia: {self.mesesGarantia}")

Producto1 = ProductoElectronico("Microondas",6000.00,"Mabe")
Producto1.cambiarGarantia(6)
Producto1.precioDescuento(10)
Producto1.detalles()
Producto2 = ProductoElectronico("Refrigerador",10000,"Mabe")
Producto2.precioDescuento(20)
Producto2.detalles()