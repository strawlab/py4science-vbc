from gi.repository import Gtk

def was_clicked(b, thing):
    print "clicked"
    lbl, a, b = thing
    lbl.set_text("BOOM")

w = Gtk.Window(title="Hello")
w.connect("delete-event", Gtk.main_quit)

b = Gtk.HBox()
l = Gtk.Label("I am a Label...")
btn = Gtk.Button("Click Me")
btn.connect("clicked", was_clicked, [l, 1, 5])


b.pack_start(l, expand=True, fill=True, padding=5)
b.pack_start(btn, True, True, 0)

w.add(b)
w.show_all()

Gtk.main()

