from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'E:\Program Files\Python\Scripts\geckodriver.exe')
#把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("http://www.santostang.com/2018/07/04/hello-world/")