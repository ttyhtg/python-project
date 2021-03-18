import requests
from bs4 import BeautifulSoup
from lxml import etree
link = "http://www.santostang.com/" 
headers = {'User-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
r = requests.get(link, headers = headers)
#print(r.text)

# 获取标题
soup = BeautifulSoup(r.text, "lxml") # 解析代码
title = soup.find("h1",class_="post-title").a.text.strip()
print(title)

with open("title.txt","a+") as f:
    f.write(title)
    f.close
