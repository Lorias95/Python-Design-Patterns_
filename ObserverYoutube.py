"""
Observer Desing Pattern
"""

from abc import ABCMeta, abstractmethod


#Clase Meta Observable: Tenemos funciones para añadir observadores y notificarlos
class YoutubeObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def suscribe(observer):
        """ The suscribe method"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """ The unsuscribe method"""   

    @staticmethod
    @abstractmethod
    def notify(observer):
        """ The notify method"""  

#Clase Sujeto: Se añaden los distintos sujetos con sus acciones
class Subject(YoutubeObservable):
    def __init__(self):
        self._observers = set()

    def suscribe(self, observer):
        self._observers.add(observer) 

    def unsubscribe(self, observer):
        self._observers.remove(observer)

#se añaden las notificaciones de la lista de objetos
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

#Clases observadores: Se desarrollan funciones definidas para recibir las notificaciones. 

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify (observable, *args, **kwargs):
        """Receive notification"""           

class Observer(IObserver):
    def __init__(self, observable, name):
        self.name = name
        observable.suscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("New Action:", self.name, "ha recibido", args, kwargs)      


#Estructuracion del Observador

SUBJECT = Subject()

OBSERVERA= Observer(SUBJECT, "Luis")
OBSERVERB= Observer(SUBJECT, "Diego")

SUBJECT.notify("Hola observadores", "soy un nuevo seguidor", "mi ID es:" , [56453534], 
                "Clave:" , {"a": 1, "b": 2, "c": 3})