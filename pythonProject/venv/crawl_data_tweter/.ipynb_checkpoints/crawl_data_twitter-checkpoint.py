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
import json


#%%
s = Service("C:/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_facebook\chromedriver.exe")
browser = webdriver.Chrome(service=s)
# mo thu 1 trang web
browser.get("https://twitter.com/i/flow/login")
