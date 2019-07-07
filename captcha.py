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

#print("1")

for i in range(0,6):
	#print("2")
	p = requests.get(url = URLGET)
	print(p.text)
	captcha_id = p.text.split("\"")[2]
	captcha_id = captcha_id[:-1][1:]
	#captcha id
	captcha_string = p.text.split("\"")[5]
	#math string

	print("Return Data = ", BLUE + p.text + ENDC)
	print("Captcha id = ",BLUE + captcha_id + ENDC)
	print("Math string = ",BLUE + captcha_string + " ,")
	
	captcha_answer = captchasolver(captcha_string)
	print("Answer = ",captcha_answer)

	a = '''
POST /api/Feedbacks/ HTTP/1.1
Host: 43.241.202.33:3000
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://43.241.202.33:3000/
Content-Type: application/json;charset=utf-8
Authorization: Bearer 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBrd2lrZS5tYXJ0IiwicGFzc3dvcmQiOiI3YzZhMTgwYjM2ODk2YTBhOGMwMjc4N2VlYWZiMGU0YyIsImNyZWF0ZWRBdCI6IjIwMTktMDYtMjVUMTE6MjI6MzUuMjk4WiIsInVwZGF0ZWRBdCI6IjIwMTktMDYtMjVUMTE6MjI6MzUuMjk4WiJ9LCJpYXQiOjE1NjI1MDk3NzcsImV4cCI6MTU2MjUyNzc3N30.Bqo-NG_YJ1hfqq35gKIaaCy64VmGVNtHv8ji_2aE6bvofwqi_4rXo8H_CcLzuvOe2P2DG_fejnLhOuVH-dtlS90QdvhxsZuLt8X3CvPy5WxdDXmnYRKBscwKdfoCF2zVJCNqhbkglIJslCZXtgTL9jeQzNjNJbjv2Zk0I5s4ogA
Content-Length: 69
Cookie: cookieconsent_status=dismiss;
continueCode=VoLJZm25zaE8lXOPWKAorHNtWcXIETlCLsKfguocL0ybn1M47QNkYBvDxqjr; 
io=1pUQu0B_8yP0v0fhAAzH; language=en; 
token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwiZW1haWwiOiJhZG1pbkBrd2lrZS5tYXJ0IiwicGFzc3dvcmQiOiI3YzZhMTgwYjM2ODk2YTBhOGMwMjc4N2VlYWZiMGU0YyIsImNyZWF0ZWRBdCI6IjIwMTktMDYtMjVUMTE6MjI6MzUuMjk4WiIsInVwZGF0ZWRBdCI6IjIwMTktMDYtMjVUMTE6MjI6MzUuMjk4WiJ9LCJpYXQiOjE1NjI1MDk3NzcsImV4cCI6MTU2MjUyNzc3N30.Bqo-NG_YJ1hfqq35gKIaaCy64VmGVNtHv8ji_2aE6bvofwqi_4rXo8H_CcLzuvOe2P2DG_fejnLhOuVH-dtlS90QdvhxsZuLt8X3CvPy5WxdDXmnYRKBscwKdfoCF2zVJCNqhbkglIJslCZXtgTL9jeQzNjNJbjv2Zk0I5s4ogA
Connection: close

{"UserId":1,"comment":"asd","rating":1,"captcha":"'''

	b = str(captcha_answer)
	c ='''","captchaId":'''

	d = a +b+ c + captcha_id + "}"
	#print("Posting: ", RED + d + ENDC + BLUE)
	enn = requests.post(url = URLPOST,data = d)
	print(enn.text) 


