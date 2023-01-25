BD={'camila':'clave12'}
ruta= 'bd.txt'

def escribir(datos):
 with open (ruta , 'w') as f:
   f.write(str(datos))

#Funcion para registrar a usuarios nuevos y guardarlos en la base de datos
def registro(BD):
  usuario = ''
  contraseña = ''
  usuario = input('Ingresa el usuario:     ')
  contraseña = input("Ingresa la contraseña:    ")
  BD[usuario] = contraseña
  escribir(BD)
  DevolverCredencial(usuario,contraseña)
 

#Ingreso a registrarme registro(BD)

#Funcion para devolver los datos de las credenciales recien registradas
def DevolverCredencial(usuario,contraseña):
  file = open(ruta , 'r')
  content = file.read()
  if usuario in content:
    print(f"Su usuario es {usuario}")
    print(f"Su contraseña es {contraseña} ")

#Funcion para leer toda la informacion almacenada en la base de datos
def LeerData(BD):
  file = open(ruta , 'r')
  content = file.read()
  print(BD)

  #Lee toda la data almacenada en el txt LeerData(BD)

#Funcion para ingresar credenciales ya registrados
def ingresarCredenciales():
    file = open(ruta , 'r')
    content = file.read()
    usuario = ''
    usuario = input('Ingrese su nombre de usuario: ')
    if usuario in content:
        ingresarContraseña(usuario)
    else:
        print('USUARIO INEXISTENTE. Ingrese su nombre de usuario o registrese.')


#Funcion para ingresar la contraseña que se usara en ingresarCredenciales
def ingresarContraseña(usuario):
    file = open(ruta , 'r')
    content = file.read()
    contraseña = ''
    contraseña = input('Ingrese su contraseña: ')
    if contraseña in content:
      imprimirBienvenida(usuario)
    else:
      print('CONTRASEÑA INCORRECTA. Restablezca su contraseña.')

#Funcion login que se utilizara para logearse en el sitio
def login():
  ingresarCredenciales()

#Funcion para imprimir solo el nombre de usuario
def imprimirBienvenida(usuario):
   file = open(ruta , 'r')
   content = file.read()
   if usuario in content:
    print(f"Bienvenido {usuario}")

#Pruebo la funcion login
login()