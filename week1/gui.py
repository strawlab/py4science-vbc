from gi.repository import Gtk

import getfile
getfile.get_from_strawlab("week1/lena-color.png")
getfile.get_from_strawlab("week1/lena-gray.png")

class App:
    def __init__(self):
        ui = Gtk.Builder()
        ui.add_from_file("gui.ui")
        ui.connect_signals(self)

        self.label = ui.get_object("label1")
        self.image = ui.get_object('image1')
        self.on_button_clicked()

        window = ui.get_object('window1')
        window.connect('destroy', lambda x: Gtk.main_quit())
        window.show_all()

    def on_button_clicked(self, *args):
        lena = "lena-color.png" if self.label.get_text() == "lena-gray.png" else "lena-gray.png"
        self.image.set_from_file(lena)
        self.label.set_text(lena)

app = App()
Gtk.main()
