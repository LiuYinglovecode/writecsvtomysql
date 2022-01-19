#!/bin/bash
# run this script if using divided method, using this file or setup_env.sh(don't need to run both)
VERSION=$(virtualenv --version | awk '{print $(NF-2);exit}')

var1=$(echo ${VERSION} | cut -f1 -d.)

var2="not found"

result=$(echo $var1 | grep "{$var2}")

if [[ "result" != "" ]]
then 
  echo "include virtualenv, no need to install"
else
  echo "no virtualenv, installing..."
  pip3 install virtualenv
fi

vtwo=$(virtualenv --version | awk '{print $(NF-2);exit}')
var3=$(echo ${vtwo} | cut -f1 -d.)
if [ $var3 -ge 20 ]
then 
  echo "no need"
  virtualenv csvpro
else 
  echo "need"
  virtualenv --no-site-packages csvpro
fi

source ./csvpro/bin/activate

# check if need to install requests
NONEED=$(pip freeze | grep requests)
if [ $NONEED ]
then
  echo "no need to install requirements" 
else
  pip install -r requirements.txt
fi

python3 call_pycsv.py 

deactivate
