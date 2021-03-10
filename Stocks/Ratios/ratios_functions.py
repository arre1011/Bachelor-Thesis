from DB.DB_Api.Get import Functions as RatiosFunctions
from DB.DB_Api.Get import StockPrice as Functions

def get_date_year_before(date):
    if( date == "2020-09-30" ):
        return "2019-09-30"
    x = date[2] + date[3]
    y = int(x)-1
    return date.replace(str(x), str(y))

def get_return_on_investment(ticker, currentDate):

    oneDateYearEarlier = get_date_year_before(currentDate)
    print(oneDateYearEarlier)

    currentYear = Functions.get_stock_price(ticker, currentDate)
    oneYearEarlyer = Functions.get_stock_price(ticker, oneDateYearEarlier)

    return str((float(currentYear) - float(oneYearEarlyer)) / float(oneYearEarlyer) * 100)


def price_per_earnings(symbol, quarterly, object):

    net_income = RatiosFunctions.get_net_income(symbol, quarterly)

    #print("Net Income: " + net_income + " Symbole: " + symbol + " Quarterly: " + quarterly)

    dividends_paid = RatiosFunctions.get_dividende_is_paid(symbol, quarterly)

    #print("Dividende Paid: " + dividends_paid + " Symbole: " + symbol + " Quarterly: " + quarterly)

    outstanding_shares = RatiosFunctions.get_outstanding_shares(symbol, object)

    #print("Outstanding Shares: " + str(outstanding_shares) + " Symbole: " + symbol + " Quarterly: " + quarterly)

    x = (float(net_income) + float(dividends_paid))

    #print("x: " + str(x))

    y = float(outstanding_shares)

    #print("y: " + str(y))

    earnings_per_share = x / y

    #print("Earning per Share: " + str(earnings_per_share) + " Symbole: " + symbol + " Quarterly: " + quarterly)

    share_price = 132.49

    return str(share_price / earnings_per_share)




