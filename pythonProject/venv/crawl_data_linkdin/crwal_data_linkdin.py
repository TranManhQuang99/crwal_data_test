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
    credential = open('login_Quang.txt')
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



def search_linkdin(key_word):
    # key_word = input("Từ khoá : ")

    browser.find_element(By.CLASS_NAME, 'global-nav__content').click()
    sleep(2)
    click_findkey = browser.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/button')
    click_findkey.click()
    sleep(3)
    search_line = browser.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    sleep(2)
    search_line.send_keys(key_word)
    sleep(3)
    search_line.send_keys(Keys.RETURN)
    sleep(4)
    browser.find_element(By.XPATH,'//*[@aria-label="Jobs"]').click()
    sleep(4)


def get_url_profile():
    page_source = BeautifulSoup(browser.page_source,"html.parser")
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




def get_url_all_page():
    number_page = int(input("số trang : "))
    url_all_page = []
    for i in range(number_page):
        url_one_page =  get_url_profile()
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(2)
        try:
            next_button = browser.find_element(By.XPATH,f'//*[@aria-label="Page {i+1}"]')
            next_button.click()
            sleep(3)
        except:
            pass
        for i in url_one_page:
            if i not in url_all_page:
                url_all_page.append(i)

        sleep(2)

    return url_all_page





def crawl_data_json(key_word):
    url_all_page = get_url_all_page()
    STT = 0
    for linkdin_url in url_all_page:
        STT += 1
        browser.get(linkdin_url)
        sleep(3)
        
        #  Show all post
        try:
            see_more = browser.find_element(By.CLASS_NAME, 'artdeco-card__action')
            sleep(1)
        except:
            continue
        see_more.click()
        sleep(2)
        page_source_company = BeautifulSoup(browser.page_source, "html.parser")
        info_div = page_source_company.find('div', class_="p5")
        try:
            name_job = info_div.find('h1').get_text().strip()
        except:
            name_job = '////'


        # get  name company
        name_company = info_div.find('div', class_="mt2")
        try:
            company = name_company.find('a').get_text().strip()
        except:
            info_loc = name_company.find_all('span')
            company = info_loc[0].find('span').get_text().strip()

        # get location
        try:
            location = name_company.find('span', class_='jobs-unified-top-card__bullet').get_text().strip()
        except:
            location = '////'

        # get content post
        try:
            content = page_source_company.find('div', id='job-details')
            post = content.find_all('span')[1].get_text().strip()
        except:
            content = page_source_company.find('div', class_='jobs-box__html-content')
            post = content.find('span').get_text().strip()

        # get id post
        Number = re.findall('\d+', linkdin_url)
        ID = Number[0]
        
        
        # get time post
        time = page_source_company.find('span', class_='jobs-unified-top-card__posted-date').get_text().strip()


        my_details = {
            'Social_Network':'Linkedin',
            'Id': ID,
            'Key_word': key_word,
            'Names': company,
            'Link_post': linkdin_url,
            'post': post,
            'comment': None,
            'device': None,
            'location': location,
            'Job_title': name_job,
            'time': time


        }
        print(my_details)


        cluster = MongoClient(
            "103.226.248.168:27017")

        cluster1 = MongoClient(
            "mongodb+srv://minh15599:123456asdf@cluster0.wkj8v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

        db = cluster1['123a']
        collection = db['myapp_employee']

        # check trung bai viet
        myquery = {"Id": ID}
        check_duplicate = []
        mydoc = collection.find(myquery)
        for i in mydoc:
            check_duplicate.append(i)
        if check_duplicate == []:
            collection.insert_one(my_details)
        else:
            continue



def main():
    login_linkdin()
    sleep(2)
    key_word = input("Từ khoá : ")
    search_linkdin(key_word)
    crawl_data_json(key_word)
    browser.close()

if __name__ == '__main__':
    main()
