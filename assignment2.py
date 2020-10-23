import requests
dir (requests)
from requests import *
dir (requests)
resp = requests.get("https://en.wikipedia.org/robots.txt")
x = resp.text
print("robots.txt for http://www.wikipedia.org/")
print(x)