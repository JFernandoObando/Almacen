import sys
#importar la clase Person de persona.py 
from persona import Person

#Importacion de librerias para utilizar pyro
import Pyro4
import Pyro4.util

#importar la clase almacen de ware.py 
from ware import almacen

#instalcion de esxcepthook para trabjar con excepciones
sys.excepthook=Pyro4.util.excepthook

#ubicacion del objeto del almacén automáticamente debido al servidor de nombres
almacen = Pyro4.Proxy("PYRONAME:ejemplo.almacen")

#llamada a los metodos de persona.py
janet = Person("Janet")
henry = Person("Henry")
janet.visit(almacen)
henry.visit(almacen)