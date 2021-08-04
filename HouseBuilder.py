"""
Builder Desing Pattern
"""

from abc import ABCMeta, abstractmethod

#Clase Director: Se encarga de construir uno o varios objetos utilizando el Constructor (Builder).

class IHouseBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def set_wall_material(self, value):
        "Set the wall_material"

    @staticmethod
    @abstractmethod
    def set_building_type(self, value):
        "Set building_type"

    @staticmethod
    @abstractmethod
    def set_number_doors(self, value):
        "Set number_doors"

    @staticmethod
    @abstractmethod
    def set_number_windows(self, value):
        "Set number_windows"    

    @staticmethod
    @abstractmethod
    def get_result(self):
        "Return the house"

#Clase House Builder: Seria la Interfaz abstracta que permite la creación de objetos.

class HouseBuilder(IHouseBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.house = House()

    def set_wall_material(self, value):
        self.house.wall_material = value
        return self

    def set_building_type(self, value):
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        self.house.doors = value
        return self

    def set_number_windows(self, value):
        self.house.windows = value
        return self    

    def get_result(self):
        return self.house

#Clase House: Seria la Interfaz abstracta que permite la creación de los atributos de los objetos.

class House():
    "The product"        

    def __init__(self, building_type="Apartament", doors=0, windows=0, wall_material=0):
        self.wall_material = wall_material

        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return "This is a {0} {1} with {2} door(s) and {3} window(s).".format(
            self.wall_material, self.building_type, self.doors, self.windows
        )    

#Clases Concrete Builders o constructores concretos: Se encargan de la implementación concreta de la clase Builder definida 
# para cada uno de los tipos. Permite crear los objetos en concreto recopilando y creando cada una de las partes que los componen.

class WoodenHouseDirector:
    "The director, building a different representation"
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("House")\
            .set_wall_material("Wooden")\
            .set_number_doors(4)\
            .set_number_windows(6)\
            .get_result()


class GlassHouseDirector:
    "The director, building a different representation"
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("House")\
            .set_wall_material("Glass")\
            .set_number_doors(8)\
            .set_number_windows(12)\
            .get_result()

class CastleDirector:
    "The director, building a different representation"
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Castle")\
            .set_wall_material("Granite")\
            .set_number_doors(100)\
            .set_number_windows(200).get_result()                        

if __name__ == "__main__":
    
#Producto o resultado: Objeto que se ha construido tras el proceso definido por el patrón.

    WOODENHOUSE = WoodenHouseDirector.construct() 
    GLASSHOUSE = GlassHouseDirector.construct()
    CASTLE = CastleDirector.construct()

    print(WOODENHOUSE)   
    print(GLASSHOUSE)
    print(CASTLE)                            