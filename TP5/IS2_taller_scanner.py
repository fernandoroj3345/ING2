"""
import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------

"""#State class: Base State class"""
"""
class State:

	def scan(self):
		
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""#Separate class for FM state"""
"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:


	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)

#*--- Inicialmente en FM

		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

"""

import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a Memorias")
        self.radio.state = self.radio.memoriastate

#*------- Implementa barrido de estaciones memorizadas
class MemoriaState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["M1(1250 AM)", "M2(103.9 FM)", "M3(1380 AM)", "M4(89.1 FM)"]
        self.pos = 0
        self.name = "MEM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.memoriastate = MemoriaState(self)
        self.state = self.fmstate  # Inicialmente en FM

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

#*---------------------

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    # Ciclo: FM → escanea 3, cambia → MEM → escanea 4, cambia → AM → escanea 3, cambia → FM ...
    actions = [radio.scan] * 3 + [radio.toggle_amfm]  # FM
    actions += [radio.scan] * 4 + [radio.toggle_amfm]  # MEM
    actions += [radio.scan] * 3 + [radio.toggle_amfm]  # AM
    actions *= 2  # Repite ciclo

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()


"""
Agregó una clase MemoriaState que contiene memorias de AM y FM.

La secuencia de estados ahora sigue: FM → MEMORIAS → AM → FM...

El número de scan() en cada estado corresponde al número de estaciones definidas
"""