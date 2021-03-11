import pymongo

def get_total_liabilities(symbole, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Balance_Sheet')
        x = x.get('yearly')
        x = x.get(date)
    try:
        totalLiabilities = x.get("totalLiab")
    except:
        print("################## get_total_liabilities Error Ticker: " + symbole + "Datum: " + date)
        totalLiabilities ="0"

    return totalLiabilities

def get_dividende_is_paid(symbole, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Cash_Flow')
        x = x.get('yearly')
        x = x.get(date)

    return x.get("dividendsPaid")

def get_net_income(symbole, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Income_Statement')
        x = x.get('yearly')
        x = x.get(date)

    return x.get("netIncome")

def get_outstanding_shares(symbole, object):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('outstandingShares')
        x = x.get('quarterly')
        x = x.get(object)

    return x.get("shares")

def get_capital_expenditures(symbole, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        try:
            x = x.get('Financials')
            x = x.get('Cash_Flow')
            x = x.get('yearly')
            x = x.get(date)
        except:
            print("################## get_capital_expenditures Error Ticker: " + symbole + "Datum: " + date)

    return x.get("capitalExpenditures")

