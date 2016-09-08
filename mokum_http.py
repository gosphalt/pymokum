from common_headers import *
import httplib, urllib

def httpCall(http_method,url, params):
	headers = HEADERS
	params = params
	connection = httplib.HTTPSConnection(URL)
	connection.request(http_method, url, "", headers)
	response = connection.getresponse()
	data = response.read()
	return data

def whoami():
	url = "/api/v1/whoami.json"
	data = httpCall("GET", url,{})
	print data 

def hide_users(user_list):
	for user in user_list:
		print "hide user " + user + " ... "
		url = "/api/v1/users/" + user + "/hide.json"
		print httpCall("POST", url, {})

def unhide_users(user_list):
	for user in user_list:
		print "unhide user " + user + " ... "
		url = "/api/v1/users/" + user + "/hide.json"
		print httpCall("DELETE", url, {})

def block_users(user_list):
	for user in user_list:
		print "block user " + user + " ... "
		url = "/api/v1/users/" + user + "/ban.json"
		print httpCall("POST", url, {})

def unblock_users(user_list):
	for user in user_list:
		print "unblock user " + user + " ... "
		url = "/api/v1/users/" + user + "/ban.json"
		print httpCall("DELETE", url, {})