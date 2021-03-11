import pymongo

def get_total_liabilities(ticker, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Balance_Sheet')
        x = x.get('yearly')
        x = x.get(date)
    try:
        totalLiabilities = x.get("totalLiab")
    except:
        print("################## get_total_liabilities Error Ticker: " + ticker + "Datum: " + date)
        totalLiabilities = ""

    return totalLiabilities

def get_dividende_is_paid(ticker, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Cash_Flow')
        x = x.get('yearly')
        x = x.get(date)
        try:
            dividendsPaid = x.get("dividendsPaid")
        except:
            print("################## get_dividende_is_paid Error Ticker: " + ticker + "Datum: " + date)
            dividendsPaid = ""

    return dividendsPaid

def get_net_income(ticker, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Income_Statement')
        x = x.get('yearly')
        x = x.get(date)

    return x.get("netIncome")

def get_outstanding_shares(ticker, object):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('outstandingShares')
        x = x.get('annual')
        x = x.get(object)
        try:
            shares = x.get("shares")
        except:
            print("################## get_total_asset Error Ticker: " + ticker + "Object: " + object)
            shares = ""

    return shares

def get_capital_expenditures(ticker, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        try:
            x = x.get('Financials')
            x = x.get('Cash_Flow')
            x = x.get('yearly')
            x = x.get(date)
        except:
            print("################## get_capital_expenditures Error Ticker: " + ticker + "Datum: " + date)

    return x.get("capitalExpenditures")

def get_total_asset(ticker, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Balance_Sheet')
        x = x.get('yearly')
        x = x.get(date)
        try:
            totalAssets = x.get("totalAssets")
        except:
            print("################## get_total_asset Error Ticker: " + ticker + "Datum: " + date)
            totalAssets = ""

    return totalAssets

