import bson.json_util
import requests
import pymongo
import json


def create_esg_score():
    years = ["'latest'", "'2020'", "'2019'", "'2018'", "'2017'", "'2016'"]
    history = "{'History':{"
    for year in years:
        print("Add ESG score of Year:" + year)
        esg_score = input()
        history += "" + year + ": {'ESGValue': '" + esg_score + "'},"

    history = history[:-1]
    layout_esg = ",'ESGScore': " + history + "}}"

    result = layout_esg.replace("'", '"')
    return result


def add_esg_score(data):
    data_minus_1 = data[:-1]
    esg_score = create_esg_score()
    result = data_minus_1 + esg_score +"}"
    return result

print("###################################### App Startet###############################")

response = requests.get('https://eodhistoricaldata.com/api/fundamentals/DHR.us?api_token=6000bdcfd1f645.51405360')
Data = response.text

data = add_esg_score(Data)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Aktien_DB"]
mycol = mydb["Aktien"]

print(type(data))
print(data)


print(type(json.loads(data)))

x = mycol.insert_one(bson.json_util.loads(data))

print("###################################### App Ende###############################")





