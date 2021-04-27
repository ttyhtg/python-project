from pyquery import PyQuery as pq

doc1 = pq(url="http://www.baidu.com/", encoding='utf-8')
print(doc1('title'))

doc = pq(url="http://www.dygang.com/", encoding='gb2312')
print(doc('title'))
tb = doc.find('.c2')
print(tb.text())

