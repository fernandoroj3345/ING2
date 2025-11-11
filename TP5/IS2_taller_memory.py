"""

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):

		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string


	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:


	def save(self, writer):
		self.obj = writer.save()

	def undo(self, writer):
		writer.undo(self.obj)


if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar");
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n\n")


	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

	print("se invoca al <undo>")
	caretaker.undo(writer)

	print("Se muestra el estado actual")
	print(writer.content + "\n\n")

"""

import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo mejorado con historial de 4 estados
#*-------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:

	def __init__(self):
		self.history = []

	def save(self, writer):
		if len(self.history) == 4:
			self.history.pop(0)  # Elimina el más antiguo si ya hay 4
		self.history.append(writer.save())

	def undo(self, writer, index):
		if 0 <= index < len(self.history):
			memento = self.history[-(index + 1)]  # 0 es el más reciente
			writer.undo(memento)
		else:
			print(f"No hay suficiente historial para undo({index})")

if __name__ == '__main__':

	os.system("clear")
	print("Crea un objeto que gestionará la versión anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional III")
	writer.write("Resumen de patrones de diseño\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional IV (no se guarda para ver el efecto)")
	writer.write("Notas de la unidad 4\n")
	print(writer.content + "\n")

	# Recuperar el estado 0 (más reciente guardado)
	print(">>> Undo(0): volver al estado inmediatamente anterior")
	caretaker.undo(writer, 0)
	print(writer.content + "\n")

	# Recuperar el segundo más reciente (index 1)
	print(">>> Undo(1): volver dos pasos atrás")
	caretaker.undo(writer, 1)
	print(writer.content + "\n")

	# Recuperar el tercero más reciente (index 2)
	print(">>> Undo(2): volver tres pasos atrás")
	caretaker.undo(writer, 2)
	print(writer.content + "\n")

	# Intento de recuperación fuera del historial
	print(">>> Undo(3): volver cuatro pasos atrás")
	caretaker.undo(writer, 3)
	print(writer.content + "\n")

"""
Se usa una lista history para almacenar hasta 4 Memento.

Se elimina el más antiguo cuando se alcanza el límite de 4.

undo(writer, index) permite restaurar un estado específico:

0 → estado más reciente guardado

1 → anterior al reciente, etc.

Se maneja el error si el índice está fuera de rango
"""