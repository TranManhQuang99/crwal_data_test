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
import win32clipboard


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

s = Service("C:/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_facebook\chromedriver.exe")
browser = webdriver.Chrome(service=s)
# mo thu 1 trang web
browser.get(
    "https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")





def login_linkdin():
    credential = open('login_Quang.txt')
    line = credential.readlines()
    username = line[0]
    password = line[1]
    # import user name
    email_field = browser.find_element(By.ID, 'username')
    email_field.send_keys(username)
    sleep(randint(1, 3))
    # import password
    password_login = browser.find_element(By.ID, 'password')
    password_login.send_keys(password)
    sleep(randint(1, 3))
    # key in ueser name
    login_field = browser.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    login_field.click()





def search_linkdin(key_word):
    # key_word = input("Từ khoá : ")

    x = browser.find_element(By.CLASS_NAME, 'global-nav__content')
    x.click()
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
    Post = browser.find_element(By.XPATH, '//*[@aria-label="Posts"]').click()
    sleep(4)
    # browser.find_element(By.XPATH,'/html/body/div[5]/aside/section/header/div[3]/button[2]/li-icon').click()


# def get_url_profile():
#     all_url_post = []
#     # CLick vao cac post de lay the class
#     sleep(1)
#     recentList = browser.find_elements(By.CLASS_NAME, "reusable-search__result-container")
#     fBody = browser.find_element(By.ID,"search-marvel-srp-scroll-container")
#
#     for list in recentList:
#         try:
#             browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
#                                    fBody)
#             sleep(1)
#             list.click()
#             sleep(1)
#
#             # click lay link url post
#             browser.find_element(By.CLASS_NAME, 'feed-shared-control-menu__trigger').click()
#             sleep(1)
#             browser.find_element(By.CLASS_NAME, 'feed-shared-control-menu__item.option-share-via').click()
#             sleep(2)
#             # tat clipboard de pass qua err
#             browser.find_element(By.CLASS_NAME, 'artdeco-button__icon').click()
#
#             sleep(1)
#             # lay du lieu ra tu clipboard
#             win32clipboard.OpenClipboard()
#             data = win32clipboard.GetClipboardData()
#             win32clipboard.CloseClipboard()
#             all_url_post.append(data)
#         except:
#             continue
#     return all_url_post
#
#
#
#
#
#
#
#
#
# def get_url_all_page():
#     number_page = int(input("số trang : "))
#     url_all_page = []
#     for i in range(number_page):
#         try:
#             try:
#                 print(i + 1)
#                 url_one_page = get_url_profile()
#                 sleep(2)
#
#
#                 # sleep(1)
#                 # element = browser.find_element(By.CLASS_NAME, 'search-marvel-srp__content-detail-bottom-divider')
#                 # element.location_once_scrolled_into_view
#                 sleep(1)
#                 browser.find_element(By.XPATH, f'//*[@aria-label="Page {i + 1}"]').click()
#                 sleep(1.5)
#
#                 # browser.refresh()
#                 # sleep(1)
#
#                 for url in url_one_page:
#                     url_all_page.append(url)
#                 sleep(1)
#             except:
#                 browser.refresh()
#                 sleep(1)
#                 browser.find_element(By.XPATH, f'//*[@aria-label="Page {i + 1}"]').click()
#         except:
#             pass
#     return url_all_page


def get_url_all_page():
    number_page = int(input("số trang : "))
    url_all_page = []
    for i in range(number_page):
        print(i + 1)
        all_url_post = []
        sleep(3)
        recentList = browser.find_elements(By.CLASS_NAME, "reusable-search__result-container")
        fBody = browser.find_element(By.ID, "search-marvel-srp-scroll-container")

        for list in recentList:
            try:
                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       fBody)
                sleep(1)
                list.click()
                sleep(1)

                # click lay link url post
                browser.find_element(By.CLASS_NAME, 'feed-shared-control-menu__trigger').click()
                sleep(1)
                browser.find_element(By.CLASS_NAME, 'feed-shared-control-menu__item.option-share-via').click()
                sleep(2)
                # tat clipboard de pass qua err
                browser.find_element(By.CLASS_NAME, 'artdeco-button__icon').click()

                sleep(1)
                # lay du lieu ra tu clipboard
                win32clipboard.OpenClipboard()
                data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                all_url_post.append(data)

                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       fBody)
            except:
                continue

        for url in all_url_post:
            url_all_page.append(url)
        sleep(1)

        try:
            browser.find_element(By.XPATH, f'//*[@aria-label="Page {i + 2}"]').click()
        except:
            fBody = browser.find_element(By.ID, "search-marvel-srp-scroll-container")

            for x in range(3):
                browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       fBody)
                sleep(1)
            browser.find_element(By.XPATH, f'//*[@aria-label="Page {i + 2}"]').click()

            sleep(2)

    sleep(3)
    return url_all_page




def crawl_data_json(key_word):
    url_all_page = get_url_all_page()

    for linkdin_url in url_all_page:
        browser.get(linkdin_url)
        sleep(3)
        try:
            page_source = BeautifulSoup(browser.page_source, "html.parser")
            # Post
            try:
                post = page_source.find('span', class_='break-words').get_text()
            except:
                pass
            # Name post
            name_post = page_source.find('span',
                                         class_='feed-shared-actor__name t-14 t-bold hoverable-link-text t-black').get_text().strip()
            # link persion post
            link = page_source.find('a', class_='app-aware-link').get('href')

            # SHOW MORE COMMENT
            #         try:
            #             browser.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div/section/div[1]/div/div[5]/div[4]/div[3]/div[2]/button/span').click()
            #         except:
            #             continue

            all_commment = []
            all_name_comment = []
            href = []
            content = []
            # get name comment
            all_class_name_comment = page_source.find_all('span',
                                                          class_='comments-post-meta__name-text hoverable-link-text')
            for name in all_class_name_comment:
                all_name_comment.append(name.get_text().strip())

            # get href comment
            all_class_href_commnet = page_source.find_all('a',
                                                          class_='ember-view inline-flex overflow-hidden t-16 t-black t-bold tap-target')
            for url_comment in all_class_href_commnet:
                href.append('https://www.linkedin.com' + str(url_comment.get('href')))
            href = list(filter(None, href))

            # get content comment
            all_class_content_comment = page_source.find_all('div',
                                                             class_='feed-shared-inline-show-more-text comments-comment-item__inline-show-more-text')
            for class_content in all_class_content_comment:
                content.append(class_content.get_text().strip())

            # map data
            map_all_comment = map(lambda x, y, z: x + str(':') + y + str(':') + z, all_name_comment, href, content)
            for i in map_all_comment:
                all_commment.append(i)

            # time post
            time_class = page_source.find('span', 'feed-shared-actor__sub-description t-12 t-normal t-black--light')
            time_post_text = time_class.find_all('span')[2].get_text().strip()

            x = time_post_text.replace("Nov", "11")
            y = x.replace("Dec", "12")
            z = y.replace("Mar", "3")
            g = z.replace("Jun", "6")
            h = g.replace("Jun", "6")
            i = h.replace("Oct", "10")
            k = i.replace("Aug", "8")
            l = k.replace("May", "5")
            m = l.replace("Jul", "7")
            n = m.replace("Jan", "1")
            o = n.replace("Sep", "9")
            z = o.replace("Feb", "2")
            zz = z.replace("Apr", "4")
            zzz = zz.replace(" 2021", "2021")
            zzzz = zzz.replace(" 2019", "2019")
            z1 = zzzz.replace(" 2020", "2020")
            z2 = z1.replace(" 2018", "2018")
            z3 = z2.replace(" ", ",")

            RE_URL = re.findall('\d+', z3)

            if len(RE_URL) == 5:
                time_post = RE_URL[-2] + str('/') + RE_URL[-3] + str('/') + RE_URL[-1]
            else:
                time_post = RE_URL[-1] + str('/') + '12/2021'


            # ID post

            RE_URL = re.findall('\d+', linkdin_url)
            for i in RE_URL:
                count_len = len(i)
                if count_len == 19:
                    ID_POST = i

            my_details = {
                'Social_Network': 'Linkedin',
                'Id': ID_POST,
                'Key_word': key_word,
                'Names': name_post,
                'Link_post': linkdin_url,
                'post': post,
                'comment': all_commment,
                'device': None,
                'location': None,
                'Job_title': None,
                'time': time_post
            }
            print(my_details)

            cluster = MongoClient(
                "103.226.248.168:27017")

            cluster1 = MongoClient(
                "mongodb+srv://minh15599:123456asdf@cluster0.wkj8v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

            db = cluster1['123a']
            collection = db['myapp_employee']



            # check trung bai viet
            myquery = {"Id": ID_POST}
            check_duplicate = []
            mydoc = collection.find(myquery)
            for i in mydoc:
                check_duplicate.append(i)
            if check_duplicate == []:
                collection.insert_one(my_details)
            else:
                continue

        except:
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


