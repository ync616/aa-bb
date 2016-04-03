import urllib 
import json
import sys
import random

word = sys.argv[1]

url = "http://api.wordnik.com:80/v4/word.json/"+ word + "/definitions?limit=200&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"

raw_data = urllib.urlopen(url).read().lower()
data =json.loads(raw_data)


for item in data:


		print "I prefer " + item['text']




