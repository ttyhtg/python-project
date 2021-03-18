import urllib.parse

url = 'http://www.baidu.com/s'
query = {
    'wd': '鼠标'
}
print(url + '?' + urllib.parse.urlencode(query))
# http://www.baidu.com/s?wd=Python3%E6%A0%87%E5%87%86%E5%BA%93&ie=UTF-8
