from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from sentence_transformers import SentenceTransformer,util
import numpy as np

def Automatic_clicker(nagivater):
    for i in range(len(nagivater)):
        quora_id = driver.find_element_by_xpath(nagivater[i])
        quora_id.click() 

def logginer(minewine,password,username):
    for i in range(len(minewine)):
        quora_id = driver.find_element_by_xpath(minewine[i])
        quora_id.click()
        if(i== 0):
            quora_id.send_keys(username)
        elif(i == 1):
            quora_id.send_keys(password)

def machine_matcher(possible_question):
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    sentence_embeddings = model.encode(possible_question)
    vector_space_length = np.zeros([len(possible_question),len(possible_question)])
    sim_q_index = -1
    max_sim=0
    for m in range(len(sentence_embeddings)):
        main = sentence_embeddings[m]
        for n in range(len(sentence_embeddings)):
            similarity_index = util.pytorch_cos_sim(main,sentence_embeddings[n])
            if m!= n and n == 0:
                if similarity_index > max_sim:
                    max_sim = similarity_index
                    sim_q_index = n
    print("Question with most exact match: {} with {}".format(possible_question[sim_q_index],max_sim))
    return sim_q_index
    
if __name__ =="__main__":

    driver = webdriver.Chrome('/usr/bin/chromedriver')                           
    driver.get("https://www.quora.com/")
    driver.implicitly_wait(15)
    assert driver.page_source,"Page has not loaded yet"

    login_elements = ['//div[@class="regular_login"]/form/div[2]/div/input',
                      '//div[@class="regular_login"]/form/div[2]/div[2]/input',
                      '//div[@class="regular_login"]/form/div[2]/div[3]/input']
    print("Hi!! Welcome to Quora auto_question merger :)")
    user_name,password = input("Enter user_name & password: ").split()
    logginer(login_elements,password,user_name)
    driver.implicitly_wait(30)
    for l in range(1,3):

        next_page = ['/html/body/div[1]/div/div/div[2]/div/div/a[2]/div/div/div[2]',
                '/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div[2]/a[2]/div/div/div/div',
                '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div[{}]/div/div/div/div[3]/div/div[2]/div[3]/div/div/button'.format(l),
                '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div[{}]/div/div/div/div[3]/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div/div[8]/div[1]/div'.format(l)]
        Automatic_clicker(next_page)
    # requested_ques = driver.find_elements_by_xpath('//*[@id]')
    # question_id = []
    # i = int(0)
    # sub = ''
    # for x in requested_ques:
    #     if i >= 34:
    #         if i == 34:
    #             question_id.append(x.get_attribute('id'))
    #             sub = (x.get_attribute('id'))[:-1]
    #         elif(sub in x.get_attribute('id')):
    #             if(len(x.get_attribute('id')) - len(sub) <=2):
    #                 question_id.append(x.get_attribute('id'))
    #     i+=1
        main_question = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div/span').text
        possible_question = []
        possible_question.append(main_question)
    
        for i in range(2,6):
            strings = '/html/body/div[2]/div/div/div/div[2]/div[4]/div/div/div[{}]/label/span/span[1]/span/span'.format(i)
            t = driver.find_element_by_xpath(strings).text
            possible_question.append(t)

        question_index = machine_matcher(possible_question)
        print(question_index)
        temp =  '/html/body/div[2]/div/div/div/div[2]/div[4]/div/div/div[{}]/label/input'.format(question_index+2)
        mer = [temp,'/html/body/div[2]/div/div/div/div[3]/div/a']
        Automatic_clicker(mer)
        print("Done :)")
        driver.execute_script("window.history.go(-1)")
        driver.implicitly_wait(30)