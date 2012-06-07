import urllib, urllib2, cookielib
import socket


class OpenStream:

	def __init__(self, username, password):
		self.host = "live-timing.formula1.com"
		self.port = 4321
		self.username = username
		self.password = password

	def auth(self):
		cj = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		login_data = urllib.urlencode({'email' : self.username, 'password' : self.password})
		resp = opener.open('http://www.formula1.com/reg/login', login_data)
		for cookie in cj:
			if cookie.name == "USER":
				return cookie.value

	def stream(self):
		BUFFER_SIZE = 4
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.host, self.port))
		s.settimeout(2)
		while True:
			try:
				byte = s.recv(1)
				print byte
			except socket.timeout:
				s.send("\n")

stream = OpenStream("asd@asd.com", "password")
stream.auth()
print stream.stream()