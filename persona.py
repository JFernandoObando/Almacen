import sys

#Clase persona 
class Person(object):
    def __init__(self, name):
        self.name = name

    #Metodo que sera llamado de visit.py
    def visit(self, almacen):
        #menu dado por un bucle
        while True:
            print("1.- Ingrese productos")
            print("2.- Consulta productos")
            print("3.- Retiro de productos")
            print("4.- Salir")
            op=input("Elija una opcion ")
            if op == "1":
                #llamada al metodo para ingresar los productos
                self.deposit(almacen)
            if op == "2":
                #lista de los productos    
                print("El almacen contiene:", almacen.list_contents())
            if op == "3":
                #llamada al metodo para retirar los productos    
                self.retrieve(almacen)
            if op == "4":
                #Si coloca "4" sale del bucle
                break
            #opcion para una opcion incorrecta
            if op > "4":
                print("#####Opcion Incorrecta#####")
                print("Programa finalizado")
        print("Gracias, vuelve!")

    #Metodo para ingresar productos al almacen
    def deposit(self, almacen):
        print("El almacen contiene:", almacen.list_contents()) #lista de los productos actuales dentro del almacen
        producto = input("Escribe lo que deseas ingresar: ").strip()
        if producto:
            #ingreso de producto
            almacen.store(self.name, producto)

    #Metodo para retirar un producto al almacen
    def retrieve(self, almacen):
        print("El almacen contiene:", almacen.list_contents()) #lista de los productos actuales dentro del almacen
        producto = input("Escribe lo que deseas retirar: ").strip()
        if producto:
            #retiro del producto
            almacen.take(self.name, producto)