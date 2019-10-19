#!/bin/bash
bin/instance stop
rm -rf var/
cp -r var_bak/ var
doitlive play session.sh
