import csv
import datetime
import json
import re
import pandas as pd
# import ISODate as ISODate
import dateutil.parser
import numpy as np

# import ISODate as ISODate
from pandas.io import pickle
from pymongo import MongoClient

with open("rename1.csv", "r", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    stt = 0
    list_json = []
    json_arr = []
    for row in reader:
    #
    #     lang_tags = row['time']
    #     x = lang_tags.replace("Nov", "11")
    #     y = x.replace("Dec", "12")
    #     z = y.replace("Mar", "3")
    #     g = z.replace("Jun", "6")
    #     h = g.replace("Jun", "6")
    #     i = h.replace("Oct", "10")
    #     k = i.replace("Aug", "8")
    #     l = k.replace("May", "5")
    #     m = l.replace("Jul", "7")
    #     n = m.replace("Jan", "1")
    #     o = n.replace("Sep", "9")
    #     z = o.replace("Feb", "2")
    #     zz = z.replace("Apr", "4")
    #     zzz = zz.replace(" 2021", "2021")
    #     zzzz = zzz.replace(" 2019", "2019")
    #     z1 = zzzz.replace(" 2020", "2020")
    #     z2 = z1.replace(" 2018", "2018")
    #     z3 = z2.replace(" ", ",")
    #
    #     RE_URL = re.findall('\d+', z3)
    #
    #     if len(RE_URL) == 5:
    #         time_post = RE_URL[-1] + str('-') + RE_URL[-3] + str('-') + RE_URL[-2]
    #     else:
    #         time_post = '2021-12' + str('-') + RE_URL[-1]

        stt = stt + 1

        # dateStr = '2016-11-11T00:00:00.000Z'
        # try:
        #     myDatetime = dateutil.parser.parse(time_post)
        # except:
        #     pass

        # format
        # try:
        #     format = '%d/%m/%Y '
        #     ddmmyy = datetime.datetime.strptime(time_post, format).date()
        # except:
        #     pass


        # def defaultconverter(o):
        #     if isinstance(o, datetime.timedelta):
        #         return o.__str__()


        my_details = {
            'Social_Network': row['Social_Network'],
            'Post_Id': row['Id'],
            'Key_word': row['Key_word'],
            'Names': row['Names'],
            'Link_post': row['Link_post'],
            'post': row['post'],
            'comment': row['comment'],
            'device': row['device'],
            'location': row['location'],
            'Job_title': row['Job_title'],
            'time': row['time'],
            'user': 'null',
            'Note': 'null',
            'id' : stt,
            "published": False


        }
        print(my_details)

        # with open('Quangdz3.json', 'a', encoding='utf-8') as f:
        #     json.dump(my_details,f,ensure_ascii=False, indent=4)

        #
        # print(my_details)
        try:
            with open('Quangdz10.json', 'a', encoding='utf-8') as f:
                json.dump(my_details, f,ensure_ascii=False, indent=4)
        except :
            pass
        # cluster = MongoClient(
        #     "mongodb+srv://minh15599:123456asdf@cluster0.wkj8v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # db = cluster['123a']
        # collection = db['django_session']
        # #
        # collection.insert_one(my_details)
        #
        # list_json.append(my_details)
        # print(list_json)

        # with open('Quangdz.json', 'a', encoding='utf-8') as f:
        #     json.(my_details, f,ensure_ascii=False, indent=4)
        # with open('Quangdz6.json', 'a') as f:
        #     json.dumps(my_details, sort_keys=True)




        # data1 = json.loads(my_details)
        # json_arr.append(my_details)
        # with open('data.json', 'w') as outfile:
        #     json.dump(json_arr, outfile)