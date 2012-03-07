
from gi.repository import Gtk

def foo(btn, lbl):
    old = int(lbl.get_text()[-1])
    lbl.set_text("Clicked %s" % (old  + 1))
    if old == 9:
        Gtk.main_quit()

w = Gtk.Window()
v = Gtk.VBox()
l = Gtk.Label("Clicked 0")

b = Gtk.Button("test")
b.connect("clicked", foo, l)

v.pack_start(l, 0, True, True)
v.pack_start(b, 0, True, True)

w.add (v)

w.show_all()

Gtk.main()
