from DB.DB_Api.Get import Functions as DBFunctions
from Stocks.Ratios import ratios_functions as RatiosFunctions
from DB.DB_Api.Get import StockPrice as Functions



class Stock:

    def __init__(self, ticker, date, object_number):
        self.symbole = ticker
        self.quarterly = date[0] + date[1] + date[2] + date[3]
        self.objectNumber = object_number
        self.totalLiabilities = DBFunctions.get_finance_variable_in_percent(ticker, date,"totalLiab" ,"Balance_Sheet")
        self.pricePerEarnings = RatiosFunctions.price_per_earnings_percent(ticker, date, object_number)
        self.capitalExpenditures = DBFunctions.get_capital_expenditures(ticker, date)
        self.stockPrice = Functions.get_stock_price(ticker, date)
        self.returnOnInvestment = RatiosFunctions.get_return_on_investment(ticker, date)
        self.bookValuePerShare = RatiosFunctions.book_value_per_share_in_percent(ticker, date, object_number)
        self.pricePerBookRatioPerShare = RatiosFunctions.price_per_book_ratio_per_share_percent(ticker, date, object_number)
        self.esgRating = DBFunctions.get_esg_rating(ticker, date)
        self.totalAssets = DBFunctions.get_finance_variable_in_percent(ticker, date, "totalAssets", "Balance_Sheet")
        self.retainedEarnings = DBFunctions.get_finance_variable_in_percent(ticker, date, "retainedEarnings", "Balance_Sheet")
        self.totalCurrentAssets = DBFunctions.get_finance_variable_in_percent(ticker, date, "totalCurrentAssets", "Balance_Sheet")
        self.totalAssets = DBFunctions.get_finance_variable_in_percent(ticker, date, "changeToLiabilities", "Cash_Flow")
        self.totalCashflowsFromInvesting = DBFunctions.get_finance_variable_in_percent(ticker, date, "totalCashflowsFromInvesting", "Cash_Flow")
        self.netIncome = DBFunctions.get_finance_variable_in_percent(ticker, date, "netIncome", "Cash_Flow")
        self.changeToNetincome = DBFunctions.get_finance_variable_in_percent(ticker, date, "changeToNetincome", "Cash_Flow")
        self.capitalExpenditures = DBFunctions.get_finance_variable_in_percent(ticker, date, "capitalExpenditures", "Cash_Flow")
        self.changeReceivables = DBFunctions.get_finance_variable_in_percent(ticker, date, "changeReceivables", "Cash_Flow")
        self.researchDevelopment = DBFunctions.get_finance_variable_in_percent(ticker, date, "researchDevelopment", "Income_Statement")
        self.incomeBeforeTax = DBFunctions.get_finance_variable_in_percent(ticker, date, "incomeBeforeTax","Income_Statement")
        self.ebit = DBFunctions.get_finance_variable_in_percent(ticker, date, "ebit","Income_Statement")
        self.grossProfit = DBFunctions.get_finance_variable_in_percent(ticker, date, "grossProfit", "Income_Statement")
        self.totalRevenue = DBFunctions.get_finance_variable_in_percent(ticker, date, "totalRevenue", "Income_Statement")
        self.costOfRevenue = DBFunctions.get_finance_variable_in_percent(ticker, date, "costOfRevenue", "Income_Statement")
        self.sector = DBFunctions.get_sector(ticker)


List = [
        "totalLiabilities",
        "pricePerEarnings",
        "capitalExpenditures",
        "bookValuePerShare",
        "pricePerBookRatioPerShare",
        "esgRating",
        "totalAssets",
        "retainedEarnings",
        "totalCurrentAssets",
        "totalAssets",
        "netIncome",
        "changeToNetincome",
        "capitalExpenditures",
        "changeReceivables",
        "researchDevelopment",
        "incomeBeforeTax",
        "ebit",
        "grossProfit",
        "totalRevenue",
        "costOfRevenue" ]

