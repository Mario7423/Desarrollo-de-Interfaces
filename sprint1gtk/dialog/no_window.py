import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class SubWindowNo(Gtk.Window):		#Ventá da resposta incorrecta
	box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	label = Gtk.Label("Respuesta incorrecta")
	
	def __init__(self):
		super().__init__(title="Ventana de respuesta")
		self.add(self.box)
		self.box.pack_start(self.label, True, True, 0)
