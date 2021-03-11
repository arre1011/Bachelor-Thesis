from DB.DB_Api.Get import Functions as RatiosFunctions
from DB.DB_Api.Get import StockPrice as Functions

def get_date_year_before(date):
    if date == "2020-03-31":
        return "2019-03-31"
    elif date == "2020-06-30":
        return "2019-06-30"
    elif date == "2020-09-30":
        return "2019-09-30"
    elif date == "2020-12-31":
        return "2019-12-31"
    elif date == "2012-12-31":
        return "2011-12-31"
    x = date[2] + date[3]
    y = int(x)-1
    return date.replace(str(x), str(y))

def get_return_on_investment(ticker, currentDate):

    oneDateYearEarlier = get_date_year_before(currentDate)
    #print(oneDateYearEarlier)

    currentYear = Functions.get_stock_price(ticker, currentDate)
    oneYearEarlyer = Functions.get_stock_price(ticker, oneDateYearEarlier)

    return str((float(currentYear) - float(oneYearEarlyer)) / float(oneYearEarlyer) * 100)

def book_value_per_share(ticker, date, object):
    totalAssets = 323888000000
    totalLiab = RatiosFunctions.get_total_liabilities(ticker, date)
    shares = RatiosFunctions.get_outstanding_shares(ticker,object)


    return (totalAssets - totalLiab) / shares

def price_per_book_Ratio_per_share(ticker, date, object):
    shares = Functions.get_stock_price(ticker, date)
    bookVlaue = book_value_per_share(ticker, date, object)

    return shares/bookVlaue


def price_per_earnings(symbol, quarterly, object):

    net_income = RatiosFunctions.get_net_income(symbol, quarterly)

   # print("Net Income: " + net_income + " Symbole: " + symbol + " Quarterly: " + quarterly)

    dividends_paid = RatiosFunctions.get_dividende_is_paid(symbol, quarterly)

    #print("Dividende Paid: " + dividends_paid + " Symbole: " + symbol + " Quarterly: " + quarterly)

    outstanding_shares = RatiosFunctions.get_outstanding_shares(symbol, object)

    #print("Outstanding Shares: " + str(outstanding_shares) + " Symbole: " + symbol + " Quarterly: " + quarterly)

    x = (float(net_income) + float(dividends_paid))

    #print("x: " + str(x))

    y = float(outstanding_shares)

    #print("y: " + str(y))

    earnings_per_share = x / y

   # print("Earning per Share: " + str(earnings_per_share) + " Symbole: " + symbol + " Quarterly: " + quarterly)

    share_price = Functions.get_stock_price(symbol, quarterly)

   # print("Share Price: " + share_price)

    return str(float(share_price) / float(earnings_per_share))




