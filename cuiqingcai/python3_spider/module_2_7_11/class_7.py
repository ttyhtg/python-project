# import requests
# r = requests.get('https://static1.scrape.cuiqingcai.com/')
# print(r.text)

import requests
r = requests.get('http://httpbin.org/get')
print(r.text)

import requests
data = {
    'name': 'germey',
    'age': 25
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)