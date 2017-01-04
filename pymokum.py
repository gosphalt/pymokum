#!/usr/bin/python

import sys
from mokum_http import *

def help():
	command = sys.argv[0]
	print command + " usage:"
	print command + " whoami -> Get your user mokum Json"
	print command + " hide <user> -> Hide <user>"
	print command + " unhide <user> -> Unhide <user>"
	print command + " block <user> -> Block <user>"
	print command + " unblock <user> -> Unblock <user>"
	print command + " post <text> -> Post a message with <text> in your board"

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
