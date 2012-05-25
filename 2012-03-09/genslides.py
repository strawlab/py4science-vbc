import glob
import os.path
import sys

template = ("-- [command=_vbc python {file}] [slide-contents-exec=source-highlight"
            " -s py -i {file} -o STDOUT --outlang-def=./pango.outlang]\n")

for p in glob.glob("*.py"):
    print template.format(file=p)
