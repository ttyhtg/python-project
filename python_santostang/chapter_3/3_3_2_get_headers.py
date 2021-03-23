import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Host': 'www.santostang.com'}
r = requests.get('http://www.santostang.com', headers=headers)
print("响应状态码：", r.status_code)