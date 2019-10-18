from selenium import webdriver
import time

browser = webdriver.Chrome('xxx/chromedriver_win32/chromedriver.exe')
browser.get('https://www.baidu.com/')
time.sleep(5)

browser.find_element_by_id("kw").send_keys("Cgrain")
browser.find_element_by_id('su').click()

time.sleep(5)
browser.quit()
