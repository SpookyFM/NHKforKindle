#! /bin/sh
_now=$(date +"%Y-%m-%d")
/usr/local/bin/python3 nhk-today.py
./kindlegen "$_now.opf"
/usr/local/bin/python3 sendmail.py