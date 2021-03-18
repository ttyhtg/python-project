from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

# # 打开Chrome浏览器
# driver = webdriver.Chrome(executable_path="E:\Program Files\python\Scripts\chromedriver.exe")
# # 浏览器最大化
# driver.maximize_window()
# # 打开首页
# driver.get('https://www.airbnb.cn/s/shenzhen/homes?refinement_paths%5B%5D=%2Fhome')
# time.sleep(3)

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'E:\Program Files\Mozilla Firefox\firefox.exe')
# 把上述地址改成你计算机中 Firefox 程序的地址

driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get("https://www.airbnb.cn/s/shenzhen/homes?refinement_paths%5B%5D=%2Fhomes")
time.sleep(3)

rent_list = driver.find_elements_by_css_selector('a._okj6x')
for eachhouse in rent_list:
    comment = eachhouse.find_elements_by_css_selector('div._2v4jmx4')
    comment = comment.text()
    price = eachhouse.find_elements_by_css_selector('div._1ixtnfc')
    price = price.text[4:]
    name = eachhouse.find_elements_by_css_selector('div._goi623')
    name = name.text
    details = eachhouse.find_elements_by_css_selector('div._wuffzwa')
    detail_list = [i.text for i in details]
    house_type = detail_list[0]
    no_bed = detail_list[1]
    no_visitor = detail_list[2]
    time.sleep(3)
    print(comment, price, name, house_type, no_bed, no_visitor)


