from abc import ABCMeta, abstractmethod

class IHouseBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def build_part_a(self, value):
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_part_b(self, value):
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_part_c(self, value):
        "Build part c"

    @staticmethod
    @abstractmethod
    def get_result(self):
        "Return the final product"

class HouseBuilder(IHouseBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('Arroz')
        return self

    def build_part_b(self):
        self.product.parts.append('Frijoles')
        return self

    def build_part_c(self):
        self.product.parts.append('Cereales')
        return self

    def get_result(self):
        return self.product

class Product():
    "The Product"

    def __init__(self):
        self.parts = []

class Director:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return HouseBuilder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

# The Client
PRODUCT = Director.construct()
print(PRODUCT.parts)

