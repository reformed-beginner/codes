#id
#text_to_transcribe
#clear_button
#submit
#transcr_output
#weak_forms
#preBracket
#postBracket

#name

from selenium import webdriver
import time

browser = webdriver.Chrome('xxx/chromedriver_win32/chromedriver.exe')
browser.get('https://tophonetics.com/')
#time.sleep(10)

browser.find_element_by_id("text_to_transcribe").send_keys("Time is a versatile performer. It flies, marches on, heals all wounds, runs out and will tell.")
browser.find_element_by_id('weak_forms').click()
browser.find_element_by_id('preBracket').send_keys('[')
browser.find_element_by_id('postBracket').send_keys(']')

browser.find_element_by_xpath('//*[@id="options_div"]/label[1]/input').click()  #British Prononciation
browser.find_element_by_id('submit').click()
#time.sleep(10)

text = browser.find_element_by_id('transcr_output').text
print(text)

#time.sleep(5)

browser.find_element_by_xpath('//*[@id="options_div"]/label[2]/input').click()  #American Prononciation
browser.find_element_by_id('submit').click()
#time.sleep(10)

text = browser.find_element_by_id('transcr_output').text
print(text)
time.sleep(5)

print('Done')
browser.quit()
