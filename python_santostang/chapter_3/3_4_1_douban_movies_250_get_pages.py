import requests


def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Host': 'movie.douban.com'}

    for i in range(0, 10):
        link = "http://movie.douban.com/top250?start=" + str(i * 25)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i+1), "页面响应状态码:", r.status_code)


get_movies()
