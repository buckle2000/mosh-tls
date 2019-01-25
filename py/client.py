#!/usr/bin/env python3
import os, sys, pexpect

if len(sys.argv) != 3:
    print(' '.join('Usage:', sys.argv[0], '<RHOST> <RPORT>'))
    exit(1)

RHOST = sys.argv[1]
RPORT = sys.argv[2]

with pexpect.spawn('ncat --ssl %s 3333 -i 0.1' % RHOST) as child:
    child.expect('MOSH CONNECT ')
    PORT, MOSH_KEY = child.readline().strip().split()
    child.close()

os.system('''MOSH_KEY=%s mosh-client %s %d''' % (MOSH_KEY.decode('ascii'), RHOST, int(PORT)))