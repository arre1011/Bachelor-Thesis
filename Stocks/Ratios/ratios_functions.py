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
    elif date == '2020-11-30':
        return '2020-11-30'
    elif date == '2020-05-31':
        return '2020-05-31'
    elif date == '2020-01-31':
        return '2020-01-31'
    elif date == '2020-07-31':
        return '2020-07-31'
    elif date == '2020-10-31':
        return '2020-10-31'
    elif date == '2020-08-31':
        return '2020-08-31'
    elif date == '2020-02-29':
        return '2020-02-29'
    x = date[2] + date[3]
    y = int(x)-1
    return date.replace(str(x), str(y))


def get_return_on_investment(ticker, currentDate):
    oneDateYearEarlier = get_date_year_before(currentDate)

    currentYear = Functions.get_stock_price(ticker, currentDate)
    oneYearEarlyer = Functions.get_stock_price(ticker, oneDateYearEarlier)

    return str((float(currentYear) - float(oneYearEarlyer)) / float(oneYearEarlyer) * 100)


def book_value_per_share(ticker, date, object):
    totalAssets = RatiosFunctions.get_total_asset(ticker, date)
    totalLiab = RatiosFunctions.get_total_liabilities(ticker, date)
    shares = RatiosFunctions.get_outstanding_shares(ticker, object)

    try:
        bookValuePerShare = (float(totalAssets) - float(totalLiab)) / float(shares)
    except:
        print("################## Function book_value_per_share: " + ticker + " Datum: " + date +
              " Total Assets: " + str(totalAssets) + " Total Liabilities: " + str(totalLiab))

    return bookValuePerShare


def price_per_book_ratio_per_share(ticker, date, object):
    shares = Functions.get_stock_price(ticker, date)
    bookVlaue = book_value_per_share(ticker, date, object)

    return float(shares)/float(bookVlaue)


def price_per_earnings(ticker, date, objectNumber):

    net_income = RatiosFunctions.get_net_income(ticker, date)
    dividends_paid = RatiosFunctions.get_dividende_is_paid(ticker, date)
    outstanding_shares = RatiosFunctions.get_outstanding_shares(ticker, objectNumber)
    #x = (float(net_income) + float(dividends_paid))
    #print("x: " + str(x))
    y = float(outstanding_shares)
    #print("y: " + str(y))
    earnings_per_share = float(net_income) / y
    share_price = Functions.get_stock_price(ticker, date)

    # print("Ticker:              " + ticker)
    # print("Date:                " + date)
    # print("Net Income:          " + net_income)
    # print("Dividende Paid:      " + dividends_paid)
    # print("Outstanding Shares:  " + str(outstanding_shares))
    # print("Earning per Share:   " + str(earnings_per_share))
    # print("Share Price:         " + share_price)

    pricePerearnings = str(float(share_price) / float(earnings_per_share))

    if float(pricePerearnings) > 0:
        return pricePerearnings
    else:
        return 0



#print("Price Per Earnings   " + price_per_earnings('MSFT', "2018-06-30", '0'))

