import re
import requests
import selenium
from bs4 import BeautifulSoup
import pyquery
import pymysql
import pymongo
import redis
import flask
import django
import jupyter
# linux: pip3 install requests selenium beautifulsoup4 pyquery pymysql pymongo redis flask django
g = requests.get('http://www.baidu.com')
print(g)