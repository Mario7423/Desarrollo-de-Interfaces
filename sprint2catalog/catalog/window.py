import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Catálogo") #Nome da ventá máis o remate do programa cando se peche.
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

        image = Gtk.Image() #Cambiado da resolución das imaxes mediante o pixbuf
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\unedited\\Corgi.jpg", 200,
            200, False)
        image.set_from_pixbuf(pixbuf)
        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\unedited\\Ovejero.jpg",
            200, 200, False)
        image2.set_from_pixbuf(pixbuf)
        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\unedited\\Boyero-de-Verna.jpg",
            200, 200, False)
        image3.set_from_pixbuf(pixbuf)
        image4 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\unedited\\Pug.jpg", 200,
            200, False)
        image4.set_from_pixbuf(pixbuf)
        image5 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            "C:\\msys64\\home\\usuario\\Desarrollo-de-Interfaces\\sprint1gtk\\catalog\\data\\unedited\\Pastor-Alemán.jpg",
            200, 200, False)
        image5.set_from_pixbuf(pixbuf)
        cell_one = Cell("Corgi", image) #Engadido das imaxes ás celdas e logo á flowbox.
        cell_two = Cell("Ovejero", image2)
        cell_three = Cell("Boyero de Verna", image3)
        cell_four = Cell("Pug", image4)
        cell_five = Cell("Pastor Alemán", image5)
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
