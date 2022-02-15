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
browser.get("https://twitter.com/i/flow/login")
sleep(5)



# def login_twitter1():
#     # lấy tài khản đăng nhập từ file login_twitter.txt
#     credential = open('C:/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_tweter\login_twitter.txt')
#     line = credential.readlines()
#     email = line[0]
#     username = line[1]
#     password = line[2]
#
#     # click ngoài trang web mới lấy được class_name login email
#     click_deteth = browser.find_element(By.XPATH, "//html").click()
#     email_login = browser.find_element(By.CLASS_NAME, "r-z2wwpe")
#     email_login.send_keys(email)
#     sleep(2)
#     email_login.send_keys(Keys.RETURN)
#     sleep(2)
#
#
#     # twitter yêu cầu nahapj tên người dùng twitter
#     click_deteth = browser.find_element(By.XPATH, "//html").click()
#     sleep(1)
#     username_login = browser.find_element(By.CLASS_NAME, "r-1kqtdi0")
#     username_login.send_keys(username)
#     username_login.send_keys(Keys.RETURN)
#     sleep(2)
#
#
#     # Nhập mật khẩu
#     click_deteth = browser.find_element(By.XPATH, "//html").click()
#     password_login = browser.find_element(By.CLASS_NAME, "r-1kqtdi0")
#     password_login.send_keys(password)
#     password_login.send_keys(Keys.RETURN)
#     sleep(2)


def login_twitter():
    # click ngoài trang web mới lấy được class_name login email
    click_deteth = browser.find_element(By.XPATH, "//html").click()
    email_login = browser.find_element(By.CLASS_NAME, "r-z2wwpe")
    email_login.send_keys("armi1xx11@gmail.com")
    sleep(1)
    email_login.send_keys(Keys.RETURN)
    sleep(1)

    # twitter yêu cầu nahapj tên người dùng twitter
    click_deteth = browser.find_element(By.XPATH, "//html").click()
    username_login = browser.find_element(By.CLASS_NAME, "r-1kqtdi0")
    username_login.send_keys("Quangdzvcl")
    username_login.send_keys(Keys.RETURN)
    sleep(1)

    # Nhập mật khẩu
    click_deteth = browser.find_element(By.XPATH, "//html").click()
    password_login = browser.find_element(By.CLASS_NAME, "r-1kqtdi0")
    password_login.send_keys("Quangtran12341@")
    password_login.send_keys(Keys.RETURN)
    sleep(1)




# tìm kiếm bài post bằng key_word

def search(key_word):
    # key_word = input("Nhập từ khoá : ")

    # click  vào ô thẻ element này mới hiện ra ô tìm kiếm từ khoá trên twitter
    browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]').click()
    sleep(1)
    search_keyword = browser.find_element(By.CLASS_NAME,"r-1dqbpge")
    search_keyword.send_keys(key_word)
    search_keyword.send_keys(Keys.RETURN)
    sleep(1)


def get_all_links():
    scorll_page = int(input("Nhập số cuộn trang : "))
    all_url_post = []
    for i in range(scorll_page):
        browser.execute_script(f'window.scrollTo(0,{i + 1}*1080)')         # Quận trang web xuống để lấy page_source
        sleep(1)
        page_source = BeautifulSoup(browser.page_source, "html.parser")
        post2 = page_source.find_all('a',
                                     class_='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-t2kpel r-1ny4l3l r-1udh08x r-ymttw5 r-1vvnge1 r-o7ynqc r-6416eg')
        post3 = page_source.find_all('a',
                                     class_='css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0')
        sleep(1)
        post_all = post2 + post3
        for url_post in post_all:
            link_url = url_post.get("href")
            link_url_full = 'https://twitter.com' + link_url
            if link_url_full not in all_url_post:
                all_url_post.append(link_url_full)
    return all_url_post




# Lấy comment trong twitter
def get_comment_replies():
    name_replies = []
    name_list_replies = []
    comment_replies = []
    comment_list_replies = []
    name_and_comment = []
    for i in range(4):
        browser.execute_script(f'window.scrollTo(0,{i}*1080)')
        page_source_twiter = BeautifulSoup(browser.page_source, "html.parser")

        info_div = page_source_twiter.find('div', class_="css-1dbjc4n r-16y2uox r-1wbh5a2 r-1ny4l3l")
        info_div2 = page_source_twiter.find_all('article',
                                                class_='css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-1udh08x r-1qhn6m8 r-i023vh r-o7ynqc r-6416eg')

        if info_div2:            # check bài viết có cmt không nếu không có thì sang bài viết khác

            info_div3 = page_source_twiter.find_all('article',
                                                    class_='css-1dbjc4n r-1loqt21 r-18u37iz r-1ut4w64 r-1ny4l3l r-1udh08x r-1qhn6m8 r-i023vh r-o7ynqc r-6416eg')
            info_div4 = info_div2 + info_div3       # cộng 2 info div vào vì comment và replies cmt là 2 thẻ div khác nhau

            for i in info_div4:

                name_replies = i.find('div',
                                      class_='css-901oao css-bfa6kz r-18u37iz r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0').get_text().strip()
                name_list_replies.append(name_replies)

                comment_replies = i.find('div',
                                         class_='css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0').get_text().strip()
                comment_list_replies.append(comment_replies)

                name_and_comment_replies = map(lambda x, y: x + str(':') + y, name_list_replies, comment_list_replies)    # map tên người cmt và nội dung cmt

                for i in name_and_comment_replies:
                    if i not in name_and_comment:
                        name_and_comment.append(i)
            sleep(1)
        else:
            break
    return name_and_comment






def crawl_data_twitter(key_word):
    STT = 0
    all_url_post = get_all_links()
    for link in all_url_post:
        STT +=1
        browser.get(link)
        sleep(5)
        page_source_twiter = BeautifulSoup(browser.page_source, "html.parser")
        info_div = page_source_twiter.find('div', class_="css-1dbjc4n r-16y2uox r-1wbh5a2 r-1ny4l3l")
        info_div2 = page_source_twiter.find('div', class_='css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l')


        # get name
        try:
            name = info_div.find('span', class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0").get_text().strip()
        except:
            name = "None"

        #get content
        try:
            try:
                post = info_div.find('div',
                                 class_="css-901oao r-1fmj7o5 r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0").get_text().strip()
            except:
                continue
        except :
            post = info_div2.find('div',
                                  class_='css-901oao r-1fmj7o5 r-37j5jr r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim r-qvutc0').get_text().strip()

        #get device
        try:
            device = info_div2.find('a',
                                   class_='css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1loqt21 r-poiln3 r-bcqeeo r-1jeg54m r-qvutc0').get_text().strip()
        except:
            device = info_div2.find('a',
                                    class_='css-4rbku5 css-18t94o4 css-901oao css-16my406 r-9ilb82 r-1loqt21 r-poiln3 r-bcqeeo r-1jeg54m r-qvutc0').get_text().strip()

        #get time
        try:
            time_class = info_div.find('div', class_='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep')
            info_loc = time_class.find_all('span')
            time_text = info_loc[0].get_text()

        except:
            time_class = info_div2.find('div', class_='css-1dbjc4n r-1awozwy r-18u37iz r-1wtj0ep')
            info_loc = time_class.find_all('span')
            time_text = info_loc[0].get_text()

        x = time_text.replace("Nov", "11")
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

        #get comment
        try:
            name_and_comment = get_comment_replies()
        except:
            name_and_comment = "None"

        Number = re.findall('\d+', link)
        ID = Number[0]


        my_details = {
            'Social_Network' : 'Twitter',
            'Id': ID,
            'Key_word': key_word,
            'Names': name,
            'Link_post': link,
            'post': post,
            'comment': name_and_comment,
            'device': device,
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
    login_twitter()
    key_word = input("Nhập từ khoá : ")
    search(key_word)
    crawl_data_twitter(key_word)
    browser.close()

if __name__ == '__main__':
    main()

