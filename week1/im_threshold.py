import sys
import argparse
import Image

import getfile

parser = argparse.ArgumentParser()
parser.add_argument('images', metavar='N', type=str, nargs='*',
                    help='images (default:lena)',
                    default=[getfile.get_from_strawlab("week1/lena-color.png")])
parser.add_argument('-t', '--threshold', type=int, default=80)
args = parser.parse_args()

for fn in args.images:
    im = Image.open(fn)
    im = im.convert('L')
    thr = im.point(lambda x: (x > args.threshold)*255)
    thr.save("binary_"+fn)

