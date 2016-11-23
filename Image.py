
import time
import threading
from Tkinter import *

"""


def worker():
	print "1--"
	#Creacicion de canvas
	canvas = Canvas(width=limitX, height=limitY, bg=colorCanvas)
	canvas.delete("all")
	canvas.pack(expand=YES, fill=BOTH)
	canvas.create_oval(10, 10, 200, 200, width=5, fill='blue')
	time.sleep(5)
	print "22"
	canvas = Canvas(width=limitX, height=limitY, bg=colorCanvas)
	canvas.pack(expand=YES, fill=BOTH)
	canvas.create_oval(10, 10, 200, 200, width=5, fill='blue')


t = threading.Thread(target=worker, name="A1")    
t.start()
 

# rectangulo

canvas = Canvas(width=300, height=210, bg='white')

canvas.pack(expand=YES, fill=BOTH)

canvas.create_rectangle(10, 10, 200, 200, width=5, fill='red')

 

# linea

canvas = Canvas(width=300, height=210, bg='white')

canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(0, 200, 200, 0, width=10, fill='green')

canvas.create_line(0, 0, 200, 200, width=10, fill='red')

 

# quesito

canvas = Canvas(width=300, height=200, bg='white')

canvas.pack(expand=YES, fill=BOTH)

canvas.create_arc(10, 10, 190, 190, start=270, extent=90, fill='gray90')

 



# arco

canvas = Canvas(root, width =300, height=200, bg='white')

canvas.pack(expand=YES, fill=BOTH)

xy = 10, 10, 190, 190

canvas.create_arc(xy, start=0, extent=270, fill='gray60')




 
"""

#


#Calse tablero
class Table():
	"""docstring for Table"""
	def __init__(self, name = "Table A"):
		#Nombre de tablero
		self.name = name

		#importamos la funcionalidad
		self.root = Tk()

		#Establecemos nombre a la ventana
		self.root.title(self.name)

		#Parametros de configuracion
		self.limitX = 400
		self.limitY = 400
		self.colorCanvas = "black"
		self.canvas = Canvas(width=self.limitX, height=self.limitY, bg=self.colorCanvas)

	def draw(self):
	
		self.canvas.pack(expand=YES, fill=BOTH)
		self.canvas.create_oval(10, 10, 200, 200, width=5, fill='blue')
		self.root.mainloop()
		



#Clase principal
class Main():
	"""docstring for Main"""
	def __init__(self, name = "" ):
		self.name = name


	def execute(self):

		table_a = Table("Game A")
		table_a.draw()

		print "End program"



linker = Main("Hola mundo")

linker.execute()