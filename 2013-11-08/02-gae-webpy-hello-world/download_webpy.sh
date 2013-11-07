#!/bin/bash

WEBPY="web.py-0.37"

wget -O - http://webpy.org/static/${WEBPY}.tar.gz | tar -xvzf -
mv ${WEBPY}/web lib/
rm -rf ${WEBPY}

