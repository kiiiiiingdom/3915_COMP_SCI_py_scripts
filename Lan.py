#!/usr/bin/python3

import os
import requests
import glob
import sys
import string

BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'


def requesting(namestring):
	try:
		p = requests.get("http://43.241.202.33:3000/i18n/" + namestring + ".json")
		if "<!DOCTYPE html>"not in p.text:
		#means theres a page exist
			#print(p.text)
			f = open(namestring + ".json", 'w')
			f.write(p.text)
			f,close();
			print(BLUE + string)
	except:
		print(RED + namestring + ENDC)

for c in string.ascii_lowercase:
	for d in string.ascii_lowercase:
		for f in string.ascii_uppercase:
			for g in string.ascii_uppercase:
				namestring = c + d + "_" + f + g
				#print("Testing: " + namestring + ENDC)
				requesting(namestring)

