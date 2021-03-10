import pymongo
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Test_DB"]
mycol = mydb["Test"]


mydict = { "name": "John", "address": "Highway 37" }

#print("Instert: " + str(mydict))

for x in mycol.find({},{  "name": 1 }):
  print(x)

#x = mycol.insert_one(mydict)

#
#
#
#
# print(type(data))
# print(data)
#
#
# print(type(json.loads(data)))
#
# x = mycol.insert_one(bson.json_util.loads(data))