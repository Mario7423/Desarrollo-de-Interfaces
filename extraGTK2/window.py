import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Aforcado")  # Nome da ventá máis o remate do programa cando se peche.
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(1200, 900)

        header = Gtk.HeaderBar(title="Aforcado")  # Formado da cabeceira.
        header.set_subtitle("A ver se acertas jajaja")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()  # Formado da ScrolledWindow.
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)
