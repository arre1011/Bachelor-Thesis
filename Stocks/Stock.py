from DB.DB_Api.Get import Functions as DBFunctions
from Ratios import ratios_functions as RatiosFunctions
from DB.DB_Api.Get import StockPrice as Functions



class Stock:

    def __init__(self, symbole, quarterly, object_number ):
        self.symbole = symbole
        self.quarterly = quarterly
        self.objectNumber = object_number
        self.totalLiabilities = DBFunctions.get_total_liabilities(symbole, quarterly)
        #self.pricePerEarnings = RatiosFunctions.price_per_earnings(symbole, quarterly, object_number)
        self.capitalExpenditures = DBFunctions.get_capital_expenditures(symbole, quarterly)
        self.stockPrice = Functions.get_stock_price(symbole, quarterly)
        self.returnOnInvestment = RatiosFunctions.get_return_on_investment(symbole, quarterly)
        #self.bookValuePerShare = RatiosFunctions.book_value_per_share(symbole, quarterly, object_number)
