import  pickle
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas
from datetime import datetime,timedelta
from selenium.webdriver.common.by import By

# khai bao bien browser

browser = webdriver.Chrome(executable_path="./chromedriver")

data = []
idx = 0
current_date = datetime(2021,9,15)

while True:
    print("process 300 days from {}-{}-{}".format(current_date.day,current_date.month,current_date.year))
    url = "https://ketqua1.net/so-ket-qua"
    browser.get(url)

    # lay theo tinh
    tinh = browser.find_element_by_id("code")

    #set_date
    end = browser.find_element_by_id("date")
    end.clear()
    end.send_keys("{}-{}-{}".format(current_date.day,current_date.month,current_date.year))

    btn = browser.find_element_by_xpath("/html/body/div[2]/div[11]/div[1]/div/div[1]/div[2]/form/div[5]/button[8]")
    btn.click()
    result = browser.find_elements_by_class_name("phoi-size.chu22.gray.need_blank.vietdam.phoi-size.chu30.maudo.stop-reload.hover")

    # click tim kiem

    for row in result:
        print(row.text)
        idx +=1
        data.append(row.text)

    current_date -= timedelta(days=300)
    if idx > 20*365:
        break
df = pd.DataFrame(data,columns=['KQ'])
df.to_csv("KQSX.csv",index=False)
browser.close()