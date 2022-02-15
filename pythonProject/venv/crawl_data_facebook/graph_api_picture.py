from requests import session
import pandas as pd
import json
from openpyxl import Workbook
import csv
import re


# import facebook
idGroup = '870665749718859'
# idGroup = '870665749718859'

s = session()
limit = 'limit(20)'


values_crawl1 = 'fields=feed.'+limit+'{comments}'
values_crawl2 = 'fields=feed.'+limit
values_crawl3 = 'comments?fields=comments.'+limit
values_crawl4 = 'fields=feed.'+limit+'{full_picture}'

token = 'EAAAAZAw4FxQIBADcnkknWtuzg606eFhisVZBMZBXoUsZCIydhp6LNLpXH8qtIaWbWDaskhj2vtYjG4G1UZAsL4PpO4gSmh1xOiKV1wzSsjUmNJruX14VHaAcXsFxBWhw5SxJK7Ildko3EnC9fehwfqxZCsvZBfEMTeuZCyELHHi4zp996swD4a0EE97Ae27FiDQZD'

data_fb1 = s.get('https://graph.facebook.com/' + idGroup + '?' + values_crawl1 + '&access_token=' + token)
data_fb2 = s.get('https://graph.facebook.com/' + idGroup + '?' + values_crawl2 + '&access_token=' + token)
data_fb3 = s.get('https://graph.facebook.com/' + idGroup + '?' + values_crawl3 + '&access_token=' + token)
data_fb4 = s.get('https://graph.facebook.com/' + idGroup + '?' + values_crawl4 + '&access_token=' + token)


# lay ảnh
s = session()
def get_picture():
    picture = []
    for i in (data_fb4.json()["feed"]["data"]):
        if 'full_picture' in i:
            picture = i['full_picture']
            id = i['id']
            img_data = s.get(picture).content
            with open('data/image_name'+ str(id)+'.jpg', 'wb') as handler:
                handler.write(img_data)

get_picture()


