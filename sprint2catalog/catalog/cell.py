import shutil

import gi
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Cell(Gtk.EventBox):
    name = None

    def __init__(self, name, description, image):
        super().__init__()
        self.name = name
        self.description = description      #Elabórase unha box con orientación vertical e engádeselle unha imaxe e un label.
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event): #Aquí compróbase qué imaxe foi escollida para amosar unha ventá con máis información.
        from detail_window import DetailWindow
        nuevaImagen = Gtk.Image()
        nuevaImagen.set_from_pixbuf(self.image.get_pixbuf())
        win = DetailWindow(Gtk.Label(self.name),nuevaImagen , Gtk.Label(self.description))
        win.show_all()
