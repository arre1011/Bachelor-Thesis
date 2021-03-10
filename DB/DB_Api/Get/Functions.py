import pymongo

def get_total_liabilities(symbole, quarterly):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Balance_Sheet')
        x = x.get('quarterly')
        x = x.get(quarterly)

    return x.get("totalLiab")

def get_dividende_is_paid(symbole, quarterly):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Cash_Flow')
        x = x.get('quarterly')
        x = x.get(quarterly)

    return x.get("dividendsPaid")

def get_net_income(symbole, quarterly):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Income_Statement')
        x = x.get('quarterly')
        x = x.get(quarterly)

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

def get_capital_expenditures(symbole,  quarterly):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": symbole})

    for x in Query:
        x = x.get('Financials')
        x = x.get('Cash_Flow')
        x = x.get('quarterly')
        x = x.get(quarterly)

    return x.get("capitalExpenditures")

