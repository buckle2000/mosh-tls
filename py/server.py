#!/usr/bin/env python3
import os, sys

if len(sys.argv) != 3:
    print('Usage:', sys.argv[0], '<PORT> <COMMAND>')
    exit(1)

PORT = sys.argv[1]
COMMAND = sys.argv[2]

os.system('''ncat --ssl -vkl localhost %s -c "mosh-server -- %s 2>/dev/null | grep 'MOSH CONNECT'"''' % (PORT, COMMAND))