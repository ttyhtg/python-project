import requests
from bs4 import BeautifulSoup
from lxml import etree
link = "http://www.santostang.com/"
headers = {'User-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
r = requests.get(link, headers=headers)
print(r.text)