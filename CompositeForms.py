"""
Composite Desing Pattern
"""

from abc import ABCMeta, abstractmethod

#Clase FormsGraphic: Clase abstracta o interfaz que deben extender o implentar tanto los objetos simples como las agrupaciones de los mismos.

class FormsGraphic(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print():
        "Print Graphics Forms"


#Clases Formas Graficas: Representación de uno o varios objetos simple. En estructura de árboles, representan las hojas de los mismos.
class Cuadrado(FormsGraphic):
    def print(self):
        print("Cuadrado")


class Rectangulo(FormsGraphic):
    def print(self):
        print("Rectangulo")


class Circulo(FormsGraphic):
    def print(self):
        print("Circulo") 

class Triangulo(FormsGraphic):
    def print(self):
        print("Triangulo")                


#Clase Composite: Representa la agrupación de los componentes, es decir, que está compuesto 
# de otros compotentes ya sean simples o compuestos.
class CompositeGraphic(FormsGraphic): 
    def __init__(self):
        self.form_graphics = [] 

    def add(self, graphic):
        self.form_graphics.append(graphic)

    def print(self):
        for g in self.form_graphics:
            g.print()          



#Estructuración de componentes

#CUADRADO1.print()
#RECTANGULO1.print()
#CIRCULO1.print()

CUADRADO1 = Cuadrado()
RECTANGULO1 = Rectangulo()
CIRCULO1 = Circulo()
TRIANGULO1 = Triangulo()

COMPOSITE1 = CompositeGraphic()
COMPOSITE1.add(CUADRADO1)
COMPOSITE1.add(CIRCULO1)
COMPOSITE1.add(TRIANGULO1)


COMPOSITE2 = CompositeGraphic()
COMPOSITE2.add(RECTANGULO1)
COMPOSITE2.add(COMPOSITE1)

COMPOSITE2.print()