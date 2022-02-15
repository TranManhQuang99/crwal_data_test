#%%
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



#%%
s = Service("C:/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_facebook\chromedriver.exe")
browser = webdriver.Chrome(service=s)
# mo thu 1 trang web
browser.get("https://twitter.com/i/flow/login")


#%%
def login_twitter():
    click_deteth = browser.find_element(By.XPATH, "//html").click()
    email_login = browser.find_element(By.CLASS_NAME, "r-z2wwpe")
    email_login.send_keys("armi1xx11@gmail.com")
    sleep(1)
    email_login.send_keys(Keys.RETURN)
    sleep(1)

    click_deteth = browser.find_element(By.XPATH, "//html").click()
    username_login = browser.find_element(By.CLASS_NAME, "r-1kqtdi0")
    username_login.send_keys("Quangdzvcl")
    username_login.send_keys(Keys.RETURN)
    sleep(1)

    click_deteth = browser.find_element(By.XPATH, "//html").click()
    password_login = browser.find_element(By.CLASS_NAME, "r-1kqtdi0")
    password_login.send_keys("Quangtran12341@")
    password_login.send_keys(Keys.RETURN)
    sleep(1)


login_twitter()

#%%
def search(key_word):
    browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]').click()
    sleep(1)
    search_keyword = browser.find_element(By.CLASS_NAME,"r-1dqbpge")
    search_keyword.send_keys(key_word)
    search_keyword.send_keys(Keys.RETURN)
    sleep(1)

search("data engineer")

#%%
all_url_post2 = []


def x():
    for i in range(10):
        browser.execute_script(f'window.scrollTo(0,{i + 1}*1080)')
        sleep(1)
        page_source = BeautifulSoup(browser.page_source, "html.parser")
        post2 = page_source.find_all('a',
                                     class_='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-t2kpel r-1ny4l3l r-1udh08x r-ymttw5 r-1vvnge1 r-o7ynqc r-6416eg')
        post3 = page_source.find_all('a',
                                     class_='css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0')
        sleep(1)
        for url_post2 in post2:
            link_url2 = url_post2.get("href")
            link_url_full = 'https://twitter.com' + link_url2
            if link_url_full not in all_url_post2:
                all_url_post2.append(link_url_full)
        for url_post3 in post3:
            link_url3 = url_post3.get("href")
            link_url_full = 'https://twitter.com' + link_url3
            if link_url_full not in all_url_post2:
                all_url_post2.append(link_url_full)
    return all_url_post2


all_url_post2 = x()


#%%

def crawl_data_twitter():
    for link in all_url_post2:
        browser.get(link)
        sleep(2)
        page_source_twiter = BeautifulSoup(browser.page_source, "html.parser")
        info_div = page_source_twiter.find('div', class_="css-1dbjc4n r-16y2uox r-1wbh5a2 r-1ny4l3l")
        try:
            name = info_div.find('span',class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0").get_text().strip()
        except:
            continue
        try:
            post = info_div.find('div',class_="css-901oao r-1fmj7o5 r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0").get_text().strip()
        except:
            continue
        print(name,post,link)
crawl_data_twitter()