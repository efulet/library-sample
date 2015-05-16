#!/bin/bash


# Script for running tests
#
# Author: Exequiel Fuentes Lettura <efulet@gmail.com>


if ! which python >/dev/null
then
  echo "It seems python is not installed on your system"
  exit 1
fi

BINPATH=`dirname $0`

# Clean environment
find ${BINPATH}/../library -type f -name '*.pyc' -delete
rm -rf Project.egg-info
rm -rf ${BINPATH}/../library/test/__pycache__

# Run test suite
python ${BINPATH}/../setup.py test
