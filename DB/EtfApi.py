import requests
import pymongo
import json

print("###################################### App Startet###############################")


etfList = {'DIA', 'DMXF', 'EAOA', 'ESGU', 'ESGD', 'ESGE', 'ESML', 'USD', 'EFAS', 'ESGS', 'FUTY', 'GRID', 'HLAL', 'ICLN'}

for x in etfList:
    print("######################################" + x + "###############################")
    nameEtf = x
    apiUrl = 'https://eodhistoricaldata.com/api/fundamentals/' + nameEtf + '.us?api_token=6000bdcfd1f645.51405360'
    response = requests.get(apiUrl)
    data = response.text

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["ETFs"]

    print(data)

    x = mycol.insert_one(json.loads(data))


print("###################################### App Ende###############################")


