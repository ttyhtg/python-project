from selenium import webdriver
import time
# 把地址改成你电脑中geckodriver.exe程序的地址 E:\Program Files\Python\Scripts
# C:\Users\Administrator\Desktop
driver = webdriver.Firefox(executable_path=r'E:\Program Files\Python\Scripts\geckodriver.exe')

#time.sleep(10)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']"))
comment = driver.find_element_by_css_selector('div.reply-content')

content = comment.find_element_by_tag_name('p')
print(content.text)
