import matplotlib.pyplot as plt
import matplotlib.animation as anim
import os.path
import pylsm.lsmreader as lsm

import getfile


if __name__ == "__main__":

    if not os.path.isfile("DB331-brain.lsm"):
        getfile.get_from_strawlab("week1/DB331-brain.lsm")
    
    lsmfile = lsm.Lsmimage("DB331-brain.lsm")
    lsmfile.open()

    Z = lsmfile.header['CZ LSM info']['Dimension Z']

    fig = plt.figure()
    layer = lsmfile.get_image(stack=0, channel=0)
    im = plt.imshow(layer, cmap=plt.cm.hot)

    def updatefig(frame, i, Z, lsmfile):
        i[0] = i[0]+1 if i[0] < Z-1 else 0
        im.set_array(lsmfile.get_image(stack=i[0], channel=0))
        return im,

    ani = anim.FuncAnimation(fig, updatefig, fargs=([0],Z,lsmfile), interval=50, blit=True) 
    plt.show()
