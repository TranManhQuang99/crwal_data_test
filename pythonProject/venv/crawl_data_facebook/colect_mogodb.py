import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient(
    "mongodb+srv://Quang:Quangtran@cluster0.fftmx.mongodb.net/Quangtran?retryWrites=true&w=majority")
db = client.test

post = {"_id": 0, "name": "quang", "score": 5}
