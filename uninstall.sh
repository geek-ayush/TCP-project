#!/bin/sh
python3 setup.py install --record files.txt
cat files.txt |xargs rm -rf
rm files.txt
echo 'TCP-server removed successfully.'