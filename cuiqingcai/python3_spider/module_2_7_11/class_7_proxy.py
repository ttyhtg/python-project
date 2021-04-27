import requests
proxies = {'http': 'http://112.195.243.224:8080', 'http': 'http://58.55.135.109:8888', }
r = requests.get('https://httpbin.org/get', proxies=proxies)
print(type(r.status_code), r.status_code)
print("----------------------")
print(type(r.headers), r.headers)
print("----------------------")
print(type(r.cookies), r.cookies)
print("----------------------")
print(type(r.url), r.url)
print("----------------------")
print(type(r.history), r.history)