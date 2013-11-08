#!/bin/bash

GDATA="gdata-2.0.18"



wget -O - http://gdata-python-client.googlecode.com/files/${GDATA}.tar.gz  | tar -xvzf -

mv ${GDATA}/src/* ./
rm -rf ${GDATA}

