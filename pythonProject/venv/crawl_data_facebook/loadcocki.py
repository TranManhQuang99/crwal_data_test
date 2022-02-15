import pickle
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



# khai bao bien browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# tắt thông báo fb
# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
# browser = webdriver.Chrome(chrome_options=chrome_options)

# openfb
browser.get("http://facebook.com/")

#load cockie form file
cockies = pickle.load(open("my_cockie.pkl","rb"))
for cockie in cockies:
    browser.add_cookie(cockie)
#refesh brower
browser.get("http://facebook.com")

# 3. Lấy link hiện comment
showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[4]/div/div/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span")
showmore_link.click()
sleep(2)
showmore_link.click()
sleep(2)
showmore_link.click()
sleep(2)

# tim tat ca cac comment ghi ra file
# comment_list = browser.find_elements_by_xpath("//div[@class='ni8dbmo4 stjgntxs l9j0dhe7']")
# sleep(2)
# for comment in comment_list:
#     #hien thi ten nguoi va noi dung :
#     data = {
#         "Ho va ten" : comment.find_element_by_class_name("pq6dq46d").text,
#         "Binh luan" : comment.find_element_by_css_selector('.ecm0bbzt.e5nlhep0.a8c37x1j').text
#     }
#     with open("fb.csv", "a", encoding='utf-8') as f:
#         f.write(f"{data['Ho va ten']};{data['Binh luan']}\n")
#     # x = comment.find_element_by_

#lay links fb
# for comment in comment_list:
#     links = comment.find_elements_by_xpath ("// a [@ class = 'nc684nl6']")
# sleep(2)
# # print(links)
# for i in links:
#     fb = i.get_attribute('href')
#     print(fb)
#
# sleep(5)
# browser.close()
#.oajrlxb2.g5ia77u1.qu
