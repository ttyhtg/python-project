from baiduspider import BaiduSpider  # 导入BaiduSpider
from pprint import pprint  # 导入pretty-print

# 获取百度的搜索结果，搜索关键词是'爬虫'
pprint(BaiduSpider().search_web('爬虫'))