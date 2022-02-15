import pickle
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
import csv
import json
import pymongo
from pymongo import MongoClient
import re


s = Service("C:/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_facebook\chromedriver.exe")
browser = webdriver.Chrome(service=s)
# mo thu 1 trang web
browser.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")



def login_linkdin():
    credential = open('login.txt')
    line = credential.readlines()
    username = line[0]
    password = line[1]
    # import user name
    email_field = browser.find_element(By.ID,'username')
    email_field.send_keys(username)
    sleep(randint(1,3))
    # import password
    password_login = browser.find_element(By.ID,'password')
    password_login.send_keys(password)
    sleep(randint(1,3))
    #key in ueser name
    login_field = browser.find_element(By.XPATH,"/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    login_field.click()
login_linkdin()
sleep(2)







key_word = 'data engineer'
def search_linkdin():
    x= browser.find_element(By.CLASS_NAME,'global-nav__content')
    x.click()
    sleep(2)
    click_findkey = browser.find_element(By.XPATH,'//*[@id="global-nav-search"]/div/button')
    click_findkey.click()
    sleep(3)
    search_line = browser.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
    sleep(2)
    search_line.send_keys(key_word)
    sleep(3)
    search_line.send_keys(Keys.RETURN)
    sleep(4)
    Post = browser.find_element(By.XPATH,'//*[@aria-label="Posts"]').click()
    sleep(2)
search_linkdin()







def get_url_profile():
    page_source = BeautifulSoup(browser.page_source, "html.parser")
    profiles_company = page_source.find_all('a',
                                            class_='disabled ember-view job-card-container__link job-card-list__title')
    all_profiles_company = []
    for profiles in profiles_company:
        profiles_company_id = profiles.get('href')
        Number = re.findall('\d+', profiles_company_id)
        ID = Number[0]
        profiles_url = 'https://www.linkedin.com/jobs/view/' + ID
        if profiles_url not in all_profiles_company:
            all_profiles_company.append(profiles_url)
    return all_profiles_company


get_url_profile()



browser.find_element(By.XPATH,'//*[@id="search-marvel-srp-scroll-container"]/div/div[1]/ul/li[1]').click()

page_source = BeautifulSoup(browser.page_source, "html.parser")
# Post
post = page_source.find('span',class_='break-words').get_text()
# Name post
name = page_source.find('span',class_='feed-shared-actor__name t-14 t-bold hoverable-link-text t-black').get_text()
link = page_source.find_all('a',class_='app-aware-link')
url_link = []
for url in link:
    url_link.append(url.get('href'))
all_url = list(dict.fromkeys(url_link))
print(all_url)








