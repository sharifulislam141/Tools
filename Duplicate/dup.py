#!/usr/bin/python
import re , urllib2  , sys , os, requests
from platform import system
from time import sleep
from threading import Thread
import time
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[38m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)


print("Duplicate Remover")
print("Telegram : @xxyz4\n")
a = raw_input('[>>] Enter Name list >> ')
c = open(a , 'r').readlines()
c_set = set(c)
aa = raw_input('[<<] Enter Name Output list >> ')
dz = open(aa , 'w')
for line in c_set:
    dz.write(line)
