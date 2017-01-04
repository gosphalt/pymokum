from common_headers import *

import httplib, urllib, json, uuid

def httpCall(http_method,url, params):
	headers = HEADERS
	params = params
	connection = httplib.HTTPSConnection(URL)
	connection.request(http_method, url, params, headers)
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
		data = httpCall("POST", url, {})
		print data

def unhide_users(user_list):
	for user in user_list:
		print "unhide user " + user + " ... "
		url = "/api/v1/users/" + user + "/hide.json"
		data = httpCall("DELETE", url, {})
		print data

def block_users(user_list):
	for user in user_list:
		print "block user " + user + " ... "
		url = "/api/v1/users/" + user + "/ban.json"
		data = httpCall("POST", url, {})
		print data

def unblock_users(user_list):
	for user in user_list:
		print "unblock user " + user + " ... "
		url = "/api/v1/users/" + user + "/ban.json"
		data = httpCall("DELETE", url, {})
		print data

def post(text, timelines=["user"], comment_disabled="false", nsfw="false"):
	url = "/api/v1/posts.json"
	params = {}
	arr_timelines = []
	obj_post = {}

	print text
	print timelines

	for tmln in timelines:
		arr_timelines.append(tmln)

	obj_post["timelines"] = arr_timelines
	obj_post["text"] = text[0]
	obj_post["comments_disabled"] = comment_disabled
	obj_post["nsfw"] = nsfw

	params["post"] = obj_post
	params["_uuid"] = str(uuid.uuid4())

	data = httpCall("POST",url, json.dumps(params))
	print data
