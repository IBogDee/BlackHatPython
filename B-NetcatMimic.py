import sys
import socket
import getopt
import threading
import subprocess

#define some global variables
listen          = False
command         = False
upload          = False
execute         = " "
target          = " "
upload_dst      = " "
port            = 0


