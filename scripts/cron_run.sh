#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit
fi

if [ -z "$1" ]
  then
    echo "No argument supplied Django base dir. Argument number 1."
fi
base=$1

if [ -z "$2" ]
  then
    echo "No argument supplied zone. Argument number 2."
fi
zone=$2

if [ -z "$3" ]
  then
    echo "No argument supplied switch (on/off). Argument number 3."
fi
switch=$3

cd "$base" || exit

poetry run python manage.py zoneOnOff "$zone" "$switch"
