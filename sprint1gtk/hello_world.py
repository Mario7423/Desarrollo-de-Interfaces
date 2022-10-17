import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
window = Gtk.Window(title="Hello World") #Título da ventá
window.show() #Amosa a ventá
window.connect("destroy", Gtk.main_quit) #Acaba cando se peche
Gtk.main()
