import requests
from requests_oauthlib import OAuth1
r = requests.get('https://static1.scrape.cuiqingcai.com/', verify=False, timeout=1)
print(type(r.status_code), r.status_code)
print("----------------------")
print(type(r.headers), r.headers)
print("----------------------")
print(type(r.cookies), r.cookies)
print("----------------------")
print(type(r.url), r.url)
print("----------------------")
print(type(r.history), r.history)