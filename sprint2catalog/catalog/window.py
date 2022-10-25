import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self, data_source):
        super().__init__(title="Catálogo") #Nome da ventá máis o remate do programa cando se peche.
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Perritos") #Formado da cabeceira.
        header.set_subtitle("Catálogo 2022")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow() #Formado da ScrolledWindow.
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        for item in data_source:
            cell = Cell(item.get("name"),item.get("description"), item.get("gtk_image"))
            self.flowbox.add(cell)
