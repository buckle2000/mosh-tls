#!/bin/sh
RHOST=127.0.0.1

CONN_STRING=`ncat --ssl $RHOST 3333 -i 0.1` 2>/dev/null
echo Connect string: $CONN_STRING
# check result has four part
# MOSH CONNECT $PORT $MOSH_KEY
(echo $CONN_STRING | python3 -c 'exit(int(len(input().split()) != 4))') || exit
PORT=`echo $CONN_STRING | python3 -c 'print(input().split()[2])'`
MOSH_KEY=`echo $CONN_STRING | python3 -c 'print(input().split()[3])'` mosh-client $RHOST $PORT