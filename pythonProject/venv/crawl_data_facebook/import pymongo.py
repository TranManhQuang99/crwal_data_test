import pymongo
from pymongo import MongoClient




cluster = MongoClient("mongodb+srv://Quang:Quangtran@cluster0.fftmx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["test"]
collections = db["test"]
post = {"_id":0,"name":"quang","score":5}
collections.insert_one(post)