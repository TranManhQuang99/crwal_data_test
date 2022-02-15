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

with open("a.csv", "r", encoding='Latin1') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        lang_tags = row['time']
        x = lang_tags.replace("Nov", "11")
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

        my_details = {
            'Social_Network': row['Social_Network'],
            'Id': row['Id'],
            'Key_word': row['Key_word'],
            'Names': row['Names'],
            'Link_post': row['Link_post'],
            'post': row['post'],
            'comment': row['comment'],
            'device': row['device'],
            'location': row['location'],
            'Job_title': row['Job_title'],
            'time': time_post,
            'user': None
        }
        print(my_details)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(my_details, f, ensure_ascii=False, indent=4)

#         cluster = MongoClient(
#             "mongodb+srv://minh15599:123456asdf@cluster0.wkj8v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#         db = cluster['123a']
#         collection = db['myapp_employee']

#         x = collection.insert_one(my_details)