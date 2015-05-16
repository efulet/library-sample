#!/bin/bash


# Script for running coverage tool
#
# Author: Exequiel Fuentes Lettura <efulet@gmail.com>


if ! which py.test >/dev/null
then
  echo "It seems py.test is not installed on your system"
  exit 1
fi

BINPATH=`dirname $0`

# Clean environment
find ${BINPATH}/../library -type f -name '*.pyc' -delete
rm -rf Project.egg-info
rm -rf ${BINPATH}/../library/test/__pycache__
rm -rf htmlcov

# Run coverage
py.test --cov=${BINPATH}/../library/lib --cov-report=term --cov-report=html
