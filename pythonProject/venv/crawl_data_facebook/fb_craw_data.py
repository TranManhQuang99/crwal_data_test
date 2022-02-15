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


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-notifications')
s = Service("C:/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_facebook\chromedriver.exe")
browser = webdriver.Chrome(service=s,options=chrome_options)
browser.implicitly_wait(10)

browser.get("https://vi-vn.facebook.com/")
cockies = pickle.load(open(r"C:\Users\armi1\PycharmProjects\pythonProject\venv\crawl_data_facebook\my_cockie.pkl","rb"))
for i in cockies:
    browser.add_cookie(i)
browser.get("https://vi-vn.facebook.com/")





key_word = 'machine learning'
def search_keyword(key_word):
    search = browser.find_element(By.CLASS_NAME,'a5nuqjux')
    search.send_keys(key_word)
    search.send_keys(Keys.RETURN)
    sleep(2)
    browser.get(f"https://www.facebook.com/search/groups?q={key_word}")

search_keyword(key_word)



def get_url_group(number_group):
    all_url_group = []
    for i in range(number_group):
        browser.execute_script(f'window.scrollTo(0,{i + 1}*1080)')
        sleep(1)
        page_source = BeautifulSoup(browser.page_source, "html.parser")
        url = page_source.find_all('a',class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p dkezsu63')
        for i in url:
            link_url = i.get('href')
            if link_url not in all_url_group:
                all_url_group.append(link_url)
    return all_url_group

all_url_group = get_url_group(1)




def join_group():
    for link in all_url_group:
        browser.get(link)
        sleep(2)
        try:
            join_group = browser.find_element(By.CSS_SELECTOR,'.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.ri2l8tne.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt.gloz99to.r516eku6.k83vx86k').click()
        except:
            continue

join_group()



def check_join_group():
    group_join = []
    for link in all_url_group:
        browser.get(link)
        sleep(1)
        page_source = BeautifulSoup(browser.page_source, "html.parser")
        try:
            join_group = page_source.find('span',
                                          class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p a57itxjd').get_text()
        except:
            continue
        if join_group == 'Đã tham gia':
            group_join.append(link)
        else:
            continue

    return group_join

group_join = check_join_group()


def convert_url():
    url_mbasic = []
    for i in group_join:
        replace_facebook = i.replace("www", "mbasic")
        url_mbasic.append(replace_facebook)

    return url_mbasic
url_mbasic = convert_url()


def get_url():
    find_id_x = []
    page_source = BeautifulSoup(browser.page_source, "html.parser")
    find_id = page_source.find_all('a', class_='dv')
    for i in find_id:
        url = i.get('href')
        find_id_x.append(url)
    return find_id_x




def get_url_post(number_post):
    url_all_post = []
    for url_group in url_mbasic:
        browser.get(url_group)
        sleep(1)
        for number in range(number_post):
            page_source = BeautifulSoup(browser.page_source, "html.parser")
            find_id = get_url()
            url_all_post = url_all_post + find_id
            sleep(2)
            try:
                x = browser.find_element(By.XPATH, '//*[@id="m_group_stories_container"]/div').click()
            except:
                continue

    return url_all_post

url_all_post = get_url_post(1)


def convert_url_link_post():
    url_post = []
    for i in url_all_post:
        replace_post_facebook = i.replace("mbasic", "www")
        url_post.append(replace_post_facebook)

    return url_post
url_post = convert_url_link_post()


def get_data_facebook():
    for url in url_post:
        browser.get(url)
        sleep(2)

        # show full comment
        try:
            browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]').click()
        except:
            browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]/span').click()
        sleep(1)
        page_source = BeautifulSoup(browser.page_source, "html.parser")

        # ten nguoi post bai
        name_post = page_source.find('span',
                                     class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain hzawbc8m').get_text()
        # Noi dung bai post
        post = page_source.find('div', class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql').get_text()
        href = page_source.find('a',
                                class_='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l oo9gr5id').get(
            'href')
        # ID nguoi viet bai
        ID = re.findall('\d+', href)[1]
        # Link fb nguoi post bai
        link_persion_post = 'https://www.facebook.com/' + ID

        # Lay ten nguoi comment
        all_comment = page_source.find('div', class_='cwj9ozl2 tvmbv18p')
        extract_cmt = all_comment.find_all('li')
        name_comment = []
        comment = []
        Link_persion_comment = []
        all_commment = []
        for li in extract_cmt:
            name_span_cmt = li.find('span',
                                    class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi lrazzd5p oo9gr5id')
            try:
                name_cmt = name_span_cmt.get_text()
                name_comment.append(name_cmt)
            except:
                continue
            try:
                span_comment = li.find('div', class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql').get_text()
                comment.append(span_comment)
            except:
                continue
            try:
                url_persion_comment = li.find('a',
                                              class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8').get(
                    'href')
                ID_persion_comment = 'https://www.facebook.com/' + re.findall('\d+', url_persion_comment)[1]
                Link_persion_comment.append(ID_persion_comment)
            except:
                continue

        map_all_comment = map(lambda x, y, z: x + str(':') + y + str(':') + z, name_comment, Link_persion_comment,
                              comment)
        for i in map_all_comment:
            all_commment.append(i)

        # ID_post
        ID_POST = re.findall('\d+', url)[0] + re.findall('\d+', url)[1]

        # Time post
        time_post_text = page_source.find('b',
                                          class_='t5a262vz nc684nl6 ihxqhq3m l94mrbxd aenfhxwr l9j0dhe7 sdhka5h4').get_text()
        try:
            Number = re.findall('\d+', time_post_text)
            time_post = Number[0] + str('/') + Number[1]
        except:
            Number = re.findall('\d+', time_post_text)
            time_post = Number[0] + str('gio truoc')

        my_details = {
            'Social_Network': 'Facebook',
            'Id': ID_POST,
            'Key_word': key_word,
            'Names': name_post,
            'Link_post': url,
            'post': post,
            'comment': all_commment,
            'device': None,
            'location': None,
            'Job_title': None,
            'time': time_post
        }
        print(my_details)

        cluster = MongoClient(
            "mongodb+srv://minh15599:123456asdf@cluster0.wkj8v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster['123a']
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


get_data_facebook()

browser.close()