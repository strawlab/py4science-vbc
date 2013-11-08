#!/bin/bash

WEBPY="web.py-0.37"

wget -O - http://webpy.org/static/${WEBPY}.tar.gz | tar -xvzf -
mv ${WEBPY}/web lib/
rm -rf ${WEBPY}

GDATA="gdata-2.0.18"

wget -O - http://gdata-python-client.googlecode.com/files/${GDATA}.tar.gz  | tar -xvzf -

mv ${GDATA}/src/* lib/
rm -rf ${GDATA}

cp -rv ../apgooglelayer lib/

cd lib
wget http://google-api-python-client.googlecode.com/files/google-api-python-client-gae-1.2.zip
unzip google-api-python-client-gae-1.2.zip
cd ..



