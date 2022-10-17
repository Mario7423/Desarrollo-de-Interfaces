import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell
#Formamos a ventá detallada das opcións dispoñibles en window

class DetailWindow(Gtk.Window):
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    label = Gtk.Label()
    image = Gtk.Image()
    label2 = Gtk.Label()

    def __init__(self, label, image, label2): #Engadimos os dous labels, un co nome e outro ca descripción, máis unha imaxe.
        super().__init__(title="Hola")
        self.add(self.box)
        self.box.pack_start(label, True, True, 0)
        self.box.pack_start(image, True, True, 0)
        self.box.pack_start(label2, True, True, 0)
