from pyquery import PyQuery as pq

doc1 = pq(url="http://www.baidu.com/", encoding='utf-8')
print(doc1('title'))

doc = pq(url="http://www.santostang.com/", encoding='gb2312')
print(doc('title'))
items = doc('.list')
lis = items.children()
print(type(lis))
print(lis)


doc2 = pq(url="http://www.cuiqingcai.com/", encoding='utf-8')
print(doc2('title'))
items = doc2('.list')
lis = items.children()
print(type(lis))
print(lis)

