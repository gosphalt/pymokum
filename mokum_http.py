from common_headers import *
import httplib, urllib

def httpCall(http_method,url, params):
	headers = HEADERS
	params = params
	connection = httplib.HTTPSConnection(URL)
	connection.request(http_method, url, "", headers)
	response = connection.getresponse()
	data = response.read()

def whoami():
	url = "/api/v1/whoami.json"
	httpCall("GET", url,{}) 
