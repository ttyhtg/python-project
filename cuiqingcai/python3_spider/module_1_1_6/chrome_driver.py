from selenium import webdriver
import time
import re
import coutries

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D/?Stats')
time.sleep(15)
page = driver.page_source
# states_list = re.findall("China", page)
# states_all = []
# for state in states_list:
#     print(state)
#     states_all.append(state)
#
# print(states_list)
print(page)
# driver.close()