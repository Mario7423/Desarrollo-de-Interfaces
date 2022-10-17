import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window): #Créanse 2 box para logo colocar unha dentro doutra
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    label = Gtk.Label("2+2 = 4?")
    button = Gtk.Button(label="Si")
    button2 = Gtk.Button(label="No")

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.button.connect("clicked", self.on_button_clicked)
        self.button2.connect("clicked", self.on_button_clicked2)
        self.add(self.box)                      #Engadimos o label á primeira box, máis a outra box cos dous botóns.
        self.box.pack_start(self.label, True, True, 0)
        self.box.pack_start(self.box2, True, True, 0)
        self.box2.pack_start(self.button, True, True, 0)
        self.box2.pack_start(self.button2, True, True, 0)

    def on_button_clicked(self, widget): #Dependendo de se se clicka Sí ou Non, abrirase unha ventá ou outra
        from yes_window import SubWindowYes
        win2 = SubWindowYes()
        win2.show_all()

    def on_button_clicked2(self, widget):
        from no_window import SubWindowNo
        win3 = SubWindowNo()
        win3.show_all()
