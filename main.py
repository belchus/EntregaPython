from mi_primer_paquete.login  import login
from mi_primer_paquete.client import Cliente
from mi_primer_paquete.client import Producto


 
#login()

#Pruebo la clase para modelar un cliente y su metodo
cliente1 = Cliente('Camila','camila','cami@coder.com',4,3506)
print(cliente1)

#Pruebo para modelar un producto
producto1=Producto(1,'Cadenita Moon',3690)
print(producto1)

producto2=Producto(2,'Pulsera Dark',2300)

producto3=Producto(3,'Aros Fly',2700)

#Pruebo el metodo para agregar un producto al carrito del usuarip
cliente1.agregoAlCarrito(producto1)

