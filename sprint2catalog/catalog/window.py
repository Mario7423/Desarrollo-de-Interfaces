import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from tkinter import messagebox as Messagebox

def cajaMensaje(widget): # Creación da MessageBox
    Messagebox.showinfo("Acerca de desarrollador?", "Nada!")
class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self, data_source):
        super().__init__(title="Catálogo")  # Nome da ventá máis o remate do programa cando se peche.
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        mb = Gtk.MenuBar() # Formado do menú

        ayudamenu = Gtk.Menu()
        ayudam = Gtk.MenuItem("Ayuda") # Engadimos axuda ao menú
        ayudam.set_submenu(ayudamenu)

        acerca = Gtk.MenuItem("Acerca de")
        acerca.connect("activate", cajaMensaje)
        ayudamenu.append(acerca) # Engadimos acerca dentro de axuda

        mb.append(ayudam)

        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        header = Gtk.HeaderBar(title="Perritos") #Formado da cabeceira.
        header.set_subtitle("Catálogo 2022")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow() #Formado da ScrolledWindow.
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        vbox.add(scrolled) #Engadimos cada box dentro da correspondente
        self.add(vbox)

        for item in data_source:
            cell = Cell(item.get("name"),item.get("description"), item.get("gtk_image")) # Engadimos as celdas obtidas grazas ao json
            self.flowbox.add(cell)
