# -*- coding: UTF-8 -*-

import collections
import random
import math
import time

from gi.repository import Gtk, GLib

class mpl:
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

class UI:
    def __init__(self, sampleinterval=0.1, timewindow=10., size=(600,350)):
        #JOHN: builder and gtkwindow, builder.connect_signals
        b = Gtk.Builder()
        b.add_from_file("myui.ui")
        b.connect_signals(self)
        
        w = b.get_object("window1")
        w.set_default_size(*size)
        
        b.get_object("label1").set_markup("<span font='20'>𐏃</span>")

        w.connect("delete-event", Gtk.main_quit)
        
        box = b.get_object("box1")
        
        # Data management
        self.offset = 0
        interval = int(sampleinterval*1000)
        bufsize = int(timewindow/sampleinterval)
        self.databuffer = collections.deque([0.0]*bufsize, bufsize)
        self.x = [sampleinterval*i for i in range(-bufsize+1,1)]

        # MPL stuff
        self.figure = mpl.Figure()
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.ax.grid(True)
        self.canvas = mpl.FigureCanvas(self.figure)
        self.line, = self.ax.plot(self.x, self.databuffer)
        
        #JOHN: box pack end and timeout and show
        box.pack_start(self.canvas, True, True, 0)
        w.show_all()
        
        GLib.timeout_add(100, self.getdata)
        
    def on_button1_clicked(self, btn):
        self.offset+=20

    def on_button2_clicked(self, btn):
        self.offset -= 10

    def on_button3_clicked(self, btn):
        self.offset = 0

    def getdata(self):
        frequency = 0.5
        noise = random.normalvariate(0., 1.)
        new = 10.*math.sin(time.time()*frequency*2*math.pi) + noise + self.offset

        self.databuffer.append( new )
        self.line.set_ydata(self.databuffer)
        self.ax.relim()
        self.ax.autoscale_view(False, False, True)
        self.canvas.draw()
        
        return True
    
if __name__ == "__main__":
    u = UI()
    Gtk.main()
