import sys
#Importacion de librerias para utilizar pyro
import Pyro4
@Pyro4.expose
@Pyro4.behavior(instance_mode="single") #tener un inventario de almacén persistente

#clase almacen
class almacen(object):
    #productos cargados por defecto en el almacen 
    def __init__(self):
        self.contents = ["silla", "bicicleta", "linterna", "laptop", "pc"]

    #lista de los productos en el almacen
    def list_contents(self):
        return self.contents

    #Metodo para retirar un producto al almacen
    def take(self, name, item):
        self.contents.remove(item)
        print("{0} retiro {1}.".format(name, item))

    #Metodo para ingresar productos al almacen
    def store(self, name, item):
        self.contents.append(item)
        print("{0} agrego {1}.".format(name, item))

#inicializacion del servidor Pyro para el objeto almacen
def main():
    Pyro4.Daemon.serveSimple(
            {
                almacen: "ejemplo.almacen",
                
            },
            ns = True)

if __name__=="__main__":
    main()