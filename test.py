#!/usr/bin/python3

import os
import requests
import glob
import sys
import string

BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'

URLGET = "http://43.241.202.33:3300/rest/captcha/"
URLPOST = "http://43.241.202.33:3300/api/Feedbacks/"

def captchasolver(mathString):
	return eval(mathString)

print("1")

p = requests.get('http://43.241.202.33:3000/rest/captcha/')
print(p.text)
captcha_id = p.text.split("\"")[2]
captcha_id = captcha_id[:-1][1:]
	#captcha id
captcha_string = p.text.split("\"")[5]