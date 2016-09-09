#!/usr/bin/python

import sys
from mokum_http import * 

def help():
	print sys.argv[0] + " usage:"


def main():
	if len(sys.argv) == 1:
		help()
		return

	print ";".join(sys.argv)

	command = sys.argv[1]
	args = sys.argv[2:]

	if command == "whoami":
		whoami()
	elif command == "hide":
		hide_users(args)
	elif  command == "unhide":
		unhide_users(args)
	elif  command == "block":
		block_users(args)
	elif  command == "unblock":
		unblock_users(args)
	elif command == "post":
		post(args)
	else:
		help()


main()