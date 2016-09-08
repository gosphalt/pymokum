import common_headers

print " ### mokum_http.py ###"

for header in common_headers.HEADERS.keys():
		print header + ": " + common_headers.HEADERS[header]