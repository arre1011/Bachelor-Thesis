import requests
import pymongo
import json

print("###################################### App Startet###############################")


stocksList = {'UNH'}#, 'GS', 'HD', 'MSFT', 'CRM', 'AMGN', 'MCD', 'BA', 'V', 'HON', 'UNH', 'GS','HD', 'MMM', 'JNJ', 'TRV', 'WMT', 'NKE', 'JPM', 'AAPL', 'AXP', 'PG', 'IBM', 'CVX', 'INTC','DOW', 'VZ', 'KO', 'WBA', 'WBA'}30 Items in list

for x in stocksList:
    print("######################################" + x + "###############################")
    nameStock = x
    apiUrl = 'https://eodhistoricaldata.com/api/fundamentals/' + nameStock + '.us?api_token=6000bdcfd1f645.51405360'
    response = requests.get(apiUrl)
    data = response.text

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    print(data)

    x = mycol.insert_one(json.loads(data))


print("#################################### App Ende ###############################")


