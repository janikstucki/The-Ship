# from pymongo import MongoClient

# uri = "mongodb://theship:theship1234@10.255.255.254:2021/theshipdb"

# client = MongoClient(uri)

# db = client["theshipdb"]

# col = db["vacuum-energy"]

# for doc in col.find():
#     print(doc)

from pymongo import MongoClient
import requests

uri = "mongodb://theship:theship1234@10.255.255.254:2021/theshipdb"

client = MongoClient(uri)

db = client["theshipdb"]

col = db["vacuum-energy"]

module = { "data": result }

col.delete_many({})
col.insert_one(module)