#Creo la clase cliente con los atributos para poder modelar los clientes
class Cliente:
    def __init__(self, nombre,usuario,email,cantProductos,orden):
        self.nombre = nombre
        self.usuario= usuario
        self.email = email
        self.cantProductos = cantProductos
        self.orden = orden
        self.carrito=[]

#Creo metodo para agregar un producto al carrito del cliente
    def agregoAlCarrito(self,producto):
      self.carrito.append(producto)
      print(f"se agregó al carrito {self.carrito}")

#Creo metodo que devuelva la cantidad de productos que compro el cliente
    def __str__(self):
       return str(f"El Cliente {self.nombre} realizo una compra de {self.cantProductos} productos ")

#Como segunda opcion creo el metodo que devuelve el detalle de el numero de orden y que se lo envia al mail de el cliente
    def __str__(self):
       return str(f"El detalle de su orden N {self.orden} se ha enviado a su mail  {self.email}  ")


#Creo la clase producto con los atributos para poder moderlar el producto en la tienda
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

#Creo los metodos que me dan el detalle del producto    
    def __str__(self):
        return str(f"Producto: {self.nombre}, precio: {self.precio}")

    def __repr__(self):
        return self.id