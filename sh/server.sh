#!/bin/sh
COMMAND=ipython

echo "Command: $COMMAND"
ncat --ssl -vkl localhost 3333 -c "mosh-server -- $COMMAND 2>/dev/null | grep 'MOSH CONNECT'"