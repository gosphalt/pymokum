#!/usr/bin/python

print " ### main.py ###"

import httplib, urllib, sys
import mokum_http

def main():
	len_argv = len(sys.argv)
	if len_argv == 1:
		print "CIAONE"
	else:
		print "+".join(sys.argv[1:])

main()
