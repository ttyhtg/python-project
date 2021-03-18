import scrapy
import json
import requests
import lxml
from bs4 import BeautifulSoup
from lxml import etree
link = "https://search.jd.com/Search?keyword=%E6%B0%B4%E6%9D%AF&enc=utf-8&pvid=421c7a43831f4c4da5da4e6c91b36c3a"
headers = {'User-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}


r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "lxml")  # 解析代码
item_array = soup.select("ul[class='gl-warp clearfix'] li[class='gl-item']")
print(item_array)
# title = soup.find("h1",class_="post-title").a.text.strip()
# print(title)

with open("test.html","a+") as f:
     f.write(str(item_array))
