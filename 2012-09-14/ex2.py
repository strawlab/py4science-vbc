from gi.repository import Gtk

class UI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Window")
        self.set_default_size(600,400)

        self.l = Gtk.Label("Hello ")
        btn = Gtk.Button("Click Me")
        btn.connect("clicked", self.button_clicked)
        box = Gtk.HBox()
        box.pack_start(self.l, True, True, 0)
        box.pack_start(btn, True, True, 0)
        
        self.add(box)
        self.show_all()
        
    def button_clicked(self, btn):
        self.l.set_text("Foo")
    
    
if __name__ == "__main__":
    u = UI()
    u.connect("delete-event", Gtk.main_quit)
    Gtk.main()
