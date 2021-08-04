"""
State Desing Pattern
"""

from abc import abstractmethod, ABCMeta

#Clases InternalState o de contexto: Clases bases para la generación de los distintos estados.
class InternalState(metaclass = ABCMeta):
	@abstractmethod
	def changeState(self):
		pass

class TurnedOn(InternalState):
	def changeState(self):
		print("Encendiendo el dispositivo!!!")
		return "¡ENCENDIDO!"

class TurnedOff(InternalState):
	def changeState(self):
		print("Apagando el dispositivo!!!")
		return "¡APAGADO!"


class IncreaseVolume(InternalState):
	def changeState(self):
		print("Aumentando el volumen de la radio por 10 !!!")
		return "+10"

class DecreaseVolume(InternalState):
	def changeState(self):
		print("Disminuyendo el volumen de la radio por 10 !!!")
		return "-10"


# Clase RadioStation o AbstractState: Representa la clase o funcion que puede cambiar de estado, se encarga de abstraer 
# lo que representaria el estado actual. 
class RadioStation(InternalState):
	def __init__(self):
		self.state = None

	def getState(self):
		return self.state

	def setState(self, status):
		self.state = status

	def changeState(self):
		self.state = self.state.changeState()


#Sección de concreteState o estado concreto: Cada uno de los siguientes componentes representa un posible estado por el cual 
# los objetos puede pasar, por lo que tendremos un ConcreteState por cada estado posible.

Radio = RadioStation()
print('El estado interno de la radio actualmente es: {}'.format(Radio.getState()))

#Estados
ENCENDIDO = TurnedOn()
APAGADO = TurnedOff()

AUMENTAR_VOL = IncreaseVolume()
DISMINUIR_VOL = DecreaseVolume()

#Encendiendo la radio
print("Encendiendo la radio!")
Radio.setState(ENCENDIDO)
Radio.changeState()
print('El estado interno de la radio actualmente es: {}'.format(Radio.getState()))

#Aumentando el volumen
print("Aumentando el volumen!")
Radio.setState(AUMENTAR_VOL)
Radio.changeState()
print('El estado de volumen de la radio actualmente es de: {}'.format(Radio.getState()))

#Disminuyendo el volumen
print("Disminuyendo el volumen!")
Radio.setState(DISMINUIR_VOL)
Radio.changeState()
print('El estado de volumen de la radio actualmente es de: {}'.format(Radio.getState()))

#Apagando la radio
print("Apagando la radio!")
Radio.setState(APAGADO)
Radio.changeState()
print('El estado interno de la radio actualmente es: {}'.format(Radio.getState()))
