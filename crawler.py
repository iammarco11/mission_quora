from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time



driver = webdriver.Chrome('/usr/bin/chromedriver')                           
driver.get("https://www.quora.com/")
driver.implicitly_wait(15)
assert driver.page_source,"Page has not loaded yet"
quora_id = driver.find_element_by_xpath('//div[@class="regular_login"]/form/div[2]/div/input')
quora_id.click()
quora_id.send_keys("<email_id>")
quora_pwd = driver.find_element_by_xpath('//div[@class="regular_login"]/form/div[2]/div[2]/input')
quora_pwd.click()
quora_pwd.send_keys("<password>")
quora_login_button = driver.find_element_by_xpath('//div[@class="regular_login"]/form/div[2]/div[3]/input')
quora_login_button.click()
driver.implicitly_wait(30)
quora_answers = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/a[2]/div/div/div[2]')
quora_answers.click()
navigate_answers = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div[2]/a[2]/div/div/div/div")
navigate_answers.click()
merger_button = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[3]/div/div/button')
merger_button.click()
option = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div/div[8]/div[1]/div')
option.click()
requested_ques = driver.find_elements_by_xpath('//*[@id]')
question_id = []
i = int(0)
sub = ''
for x in requested_ques:
    if i >= 34:
        if i == 34:
            question_id.append(x.get_attribute('id'))
            sub = (x.get_attribute('id'))[:-1]
        elif(sub in x.get_attribute('id')):
            if(len(x.get_attribute('id')) - len(sub) <=2):
                question_id.append(x.get_attribute('id'))
    i+=1
print(question_id)
main_question = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/span').text
possible_question = []
possible_question.append(main_question)
for i in range(2,6):
    strings = '/html/body/div[2]/div/div/div/div[2]/div[4]/div/div/div[{}]/label/span/span[1]/span/span'.format(i)
    t = driver.find_element_by_xpath(strings).text
    possible_question.append(t)
print(possible_question)
