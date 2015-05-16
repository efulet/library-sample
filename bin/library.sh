#!/bin/bash


# Script for running my coding exercise
#
# Author: Exequiel Fuentes Lettura <efulet@gmail.com>

BINPATH=`dirname $0`

python ${BINPATH}/../library/library.py "$@"
