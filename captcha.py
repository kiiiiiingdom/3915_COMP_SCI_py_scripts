
#!/usr/bin/python3

import os
import requests
import glob
import sys
import string

BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'

URLGET = "http://43.241.202.33:3000/rest/captcha/"
URLPOST = "http://43.241.202.33:3000/api/Feedbacks/"

def captchasolver(mathString):
	return eval(mathString)

for i in range(0,50):
	p = requests.get(url = URLGET)
	captcha_id = p.text.split("\"")[2]
	captcha_id = captcha_id[:-1][1:]
	#captcha id
	captcha_string = p.text.split("\"")[5]
	#math string

	print("Return Data = " + p.text)
	print("Captcha id = " + captcha_id)
	print("Math string = " + captcha_string)
	
	captcha_answer = captchasolver(captcha_string)
	print("Answer = " + str(captcha_answer))

	headers = {
		'Host': '43.241.202.33:3000',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Referer': 'http://43.241.202.33:3000/administration',
		'Content-Type': 'application/json;charset=utf-8',
		'Content-Length': '56',
		'Cookie': 'cookieconsent_status=dismiss;continueCode=mnWyjRDqM8OVJE1Z5e4r9bXpaAP9HPCysld2kBLm3KwlNx6YnWgoP7zvQeRE;io=q-wn9uU_bfTf1ZCKAA1B',
		'Connection': 'keep-alive'
		}

	a1 = '''{"UserId":1,"comment":"asd","rating":1,"captcha":"'''

	b = str(captcha_answer)
	c ='''","captchaId":'''

	d = a1 + b+ c + str(captcha_id) + "}"
	#d = '''{"comment":"1","rating":1,"captcha":"''' + b + '''","captchaId":''' + "430" + '}'
	print("Posting: " + d)
	#os.system(d)
	enn = requests.post(URLPOST,data = d,headers = headers)
	print(enn.text + "..............\n") 