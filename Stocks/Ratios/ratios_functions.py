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
    y = int(x) + 1
    return date.replace(str(x), str(y))


def get_return_on_investment(ticker, dateOneYearEarlyer):
    currentDate = get_date_year_before(dateOneYearEarlyer)

    currentYear = Functions.get_stock_price(ticker, dateOneYearEarlyer)
    oneYearEarlyer = Functions.get_stock_price(ticker, currentDate)

    return str(int((float(oneYearEarlyer) - float(currentYear)) / float(currentYear) * 100))


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

def book_value_per_share_in_percent(ticker, date, object):
    dateOneYearEarlier = RatiosFunctions.calculate_one_year_before(date)

    currentValue = book_value_per_share(ticker, date, object)
    beforevalue = book_value_per_share(ticker, dateOneYearEarlier, object)

    return str(int((float(currentValue) - float(beforevalue)) / float(beforevalue) * 100))

def price_per_book_ratio_per_share(ticker, date, object):
    shares = Functions.get_stock_price(ticker, date)
    bookVlaue = book_value_per_share(ticker, date, object)

    return float(shares)/float(bookVlaue)

def price_per_book_ratio_per_share_percent(ticker, date, object):
    dateOneYearEarlier = RatiosFunctions.calculate_one_year_before(date)

    currentValue = price_per_book_ratio_per_share(ticker, date, object)
    beforevalue = price_per_book_ratio_per_share(ticker, dateOneYearEarlier, object)

    return str(int((float(currentValue) - float(beforevalue)) / float(beforevalue) * 100))


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


    pricePerearnings = str(float(share_price) / float(earnings_per_share))

    if float(pricePerearnings) > 0:
        return pricePerearnings
    else:
        return 0

def price_per_earnings_percent(ticker, date, object):
    dateOneYearEarlier = RatiosFunctions.calculate_one_year_before(date)

    currentValue = price_per_earnings(ticker, date, object)
    beforevalue = price_per_earnings(ticker, dateOneYearEarlier, object)
    if beforevalue == 0 or beforevalue is None or beforevalue == '0'or beforevalue == '0.00' or str(beforevalue) == "None":
        return "null"
    elif currentValue == 0 or currentValue is None or currentValue == '0' or currentValue == '0.00' or str(currentValue) == "None":
        return "null"

    return str(int((float(currentValue) - float(beforevalue)) / float(beforevalue) * 100))

#print("Price Per Earnings   " + book_value_per_share_in_percent('MSFT', "2020-06-30", '0'))

