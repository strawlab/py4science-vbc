#!/usr/bin/env python

from gi.repository import Gtk

import getfile
getfile.get_from_strawlab("week1/lena-color.png")
getfile.get_from_strawlab("week1/lena-gray.png")

class App(Gtk.Builder):
    def __init__(self):
        super(App, self).__init__()
        self.add_from_file("gui.ui")
        self.connect_signals(self)

        self._label = self.get_object("label1")
        self._image = self.get_object('image1')
        self._on_button_clicked()

        window = self.get_object('window1')
        window.connect('destroy', lambda x: Gtk.main_quit())
        window.show_all()

    def _on_button_clicked(self, *args):
        lena = "lena-color.png" if self._label.get_text() == "lena-gray.png" else "lena-gray.png"
        self._image.set_from_file(lena)
        self._label.set_text(lena)

app = App()
Gtk.main()
