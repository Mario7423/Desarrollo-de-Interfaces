import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow

win = MainWindow()  #Main que amosa a ventá necesaria
win.show_all()

Gtk.main()
