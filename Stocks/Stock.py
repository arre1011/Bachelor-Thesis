from DB.DB_Api.Get import Functions as DBFunctions
from Stocks.Ratios import ratios_functions as RatiosFunctions
from DB.DB_Api.Get import StockPrice as Functions



class Stock:

    def __init__(self, ticker, date, object_number):
        self.symbole = ticker
        self.quarterly = date
        self.objectNumber = object_number
        self.totalLiabilities = DBFunctions.get_total_liabilities(ticker, date)
        self.pricePerEarnings = RatiosFunctions.price_per_earnings(ticker, date, object_number)
        self.capitalExpenditures = DBFunctions.get_capital_expenditures(ticker, date)
        self.stockPrice = Functions.get_stock_price(ticker, date)
        self.returnOnInvestment = RatiosFunctions.get_return_on_investment(ticker, date)
        self.bookValuePerShare = RatiosFunctions.book_value_per_share(ticker, date, object_number)
        self.pricePerBookRatioPerShare = RatiosFunctions.price_per_book_ratio_per_share(ticker, date, object_number)
