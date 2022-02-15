import  pickle
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# khai bao bien browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
from selenium.webdriver.common.by import By

# mo thu 1 trang web
browser.get("http://facebook.com")

# dien thong tin vao user va pass
txtUser = browser.find_element(By.ID,"email")
txtUser.send_keys("nguyenxuanminh159@gmail.com")

txtpass = browser.find_element(By.ID,"pass")
txtpass.send_keys("minh10a123456")
sleep(5)
#submit from
txtpass.send_keys(Keys.ENTER)
# dung chuong trinh 5 s
sleep(10)
pickle.dump(browser.get_cookies(),open("my_cockie.pkl","wb"))