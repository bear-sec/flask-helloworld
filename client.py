import requests

host = '127.0.0.1'
port = '5000'

def talk(cmd):
	url = "http://{}:{}/coolstuff/{}"
	print requests.get(url.format(host,port,cmd.encode('base64'))).content

	
while 1:
    talk(raw_input())
