import gi 
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class MainWindow(Gtk.Window):
	flowbox = Gtk.FlowBox()
	
	def __init__(self):
		super().__init__(title="Catálogo")
		self.connect("destroy", Gtk.main_quit)
		self.set_border_width(15)
		self.set_default_size(400,400)
		
		header = Gtk.HeaderBar(title="Perritos")
		header.set_subtitle("Catálogo 2022")
		header.props.show_close_button = True
		
		self.set_titlebar(header)
		
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.flowbox)
		self.add(scrolled)
		
		cell_one = Cell("Corgi", Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Corgii-edited.jpg"))
		cell_two = Cell("Ovejero", Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Ovejero-edited.jpg"))
		cell_three = Cell("Boyero de Verna", Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Boyero-de-Verna-edited.jpg"))
		cell_four = Cell("Pug", Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Pug-edited.jpg"))
		cell_five = Cell("Pastor Alemán", Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Pastor-Alemán-edited.jpg"))
		self.flowbox.add(cell_one)
		self.flowbox.add(cell_two)
		self.flowbox.add(cell_three)
		self.flowbox.add(cell_four)
		self.flowbox.add(cell_five)
		
		
