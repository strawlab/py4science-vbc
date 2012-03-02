
import Image
import sys

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print "usage: python im2Dthreshold.py treshold filename [filename2, ...]"
        exit()
    
    threshold, filenames = int(sys.argv[1]), sys.argv[2:]

    for fn in filenames:
        im = Image.open(fn)
        im = im.convert('L')
        thr = im.point(lambda x: (x > threshold)*255)
        thr.save("binary_"+fn)

