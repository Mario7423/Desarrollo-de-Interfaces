
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Cell(Gtk.EventBox):
    name = None

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        from detail_window import DetailWindow
        if self.name == "Corgi":
           win = DetailWindow(Gtk.Label("Corgi"), Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Corgii-edited.jpg"), Gtk.Label("Un perro pequeño"))
        elif self.name == "Pug":
            win = DetailWindow(Gtk.Label("Pug"), Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Pug-edited.jpg"), Gtk.Label("Un perro enano"))
        elif self.name == "Pastor Alemán":
            win = DetailWindow(Gtk.Label("Pastor Alemán"), Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Pastor-Alemán-edited.jpg"), Gtk.Label("Un perro bonito"))
        elif self.name == "Ovejero":
            win = DetailWindow(Gtk.Label("Ovejero"), Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Ovejero-edited.jpg"), Gtk.Label("Un perro peludo"))
        elif self.name == "Boyero de Verna":
            win = DetailWindow(Gtk.Label("Boyero de Verna"), Gtk.Image.new_from_file("C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\edited\\Boyero-de-Verna-edited.jpg"), Gtk.Label("Un perro fiel"))
        win.show_all()
