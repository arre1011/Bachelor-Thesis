import pymongo

def get_sector(ticker):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('General')
    try:
        sector = x.get("Sector")
    except:
        print("################## get_total_liabilities Error Ticker: " + ticker)
        sector = ""

    return sector

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


def get_esg_rating(ticker, date):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})
    date = date[0]+date[1]+date[2]+date[3]

    if int(date) <= 2016:
        for x in Query:
            x = x.get('ESGScore')
            x = x.get('History')
            x = x.get("2016")
            try:
                esgValue = x.get("ESGValue")
            except:
                print("################## get_esg_rating Error Ticker: " + ticker + "Datum: " + date)
    else:
        for x in Query:
            x = x.get('ESGScore')
            x = x.get('History')
            x = x.get(date)
            try:
               esgValue = x.get("ESGValue")
            except:
               print("################## get_esg_rating Error Ticker: " + ticker + "Datum: " + date)

    return change_esg_value_to_float(esgValue)

def get_finance_variable(ticker, date, variable_name, financel):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Aktien_DB"]
    mycol = mydb["Aktien"]

    Query = mycol.find({"General.Code": ticker})

    for x in Query:
        x = x.get('Financials')
        x = x.get(financel)
        x = x.get('yearly')
        x = x.get(date)
        try:
            variable = x.get(variable_name)
        except:
            print(" Function get_finance_variable Error Ticker: " + ticker + " Datum: " + date + " Name" + variable_name)
            variable = ""

    return variable

def get_finance_variable_in_percent(ticker , currentDate, variable_name, financel):
    dateOneYearEarlier = calculate_one_year_before(currentDate)

    currentValue = get_finance_variable(ticker, currentDate, variable_name, financel)
    beforevalue = get_finance_variable(ticker, dateOneYearEarlier, variable_name, financel)
    if beforevalue == 0 or beforevalue is None or beforevalue == '0'or beforevalue == '0.00' or str(beforevalue) == "None":
        return "null"
    elif currentValue == 0 or currentValue is None or currentValue == '0'or currentValue == '0.00'or str(currentValue) == "None":
        return "null"

    # print("beforevalue: " + str(beforevalue))
    # print(" variable_name: " + variable_name)
    # print(type(beforevalue))
    # floatCurrentValue = float(currentValue)
    # floatBeforeValue = float(beforevalue)

    return str(int((float(currentValue) - float(beforevalue)) / float(beforevalue) * 100))

def change_esg_value_to_float(esgValue):
    if esgValue == "AAA":
        return 0
    elif esgValue == "AA":
        return 1
    elif esgValue == "A":
        return 2
    elif esgValue == "BBB":
        return 3
    elif esgValue == "BB":
        return 4
    elif esgValue == "B":
        return 5
    elif esgValue == "CCC":
        return 6
    elif esgValue == "CC":
        return 7
    elif esgValue == "C":
        return 8
    return esgValue

def calculate_one_year_before(currentDate):
    yearOfDate = int(currentDate[0] + currentDate[1] + currentDate[2] + currentDate[3]) - 1
    monthAndDaysOfDate = currentDate[4] + currentDate[5] + currentDate[6] + currentDate[7] + currentDate[8] + \
                         currentDate[9]
    oneYearEarlier = str(yearOfDate) + monthAndDaysOfDate
    return oneYearEarlier
