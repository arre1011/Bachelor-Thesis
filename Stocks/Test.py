from Stock import Stock
import Helper_functions
import seaborn as sns
import matplotlib.pyplot as plt

# Company's with missing values (teh number in front of the Ticker is the index in the DB:
# (wird error :10'PYPL'), (16MRK no data in 2020 as well 23'ABT', 25'ABBV' 30'LLY', 6'JNJ'), (Month Febrary: 11'HD',

# past already 'AMZN', 'GOOGL', 'AAPL', 'MSFT', 'V', 'MA', 'PG', 'DIS', 'CMCSA', 'KO', 'ADBE', 'NKE', 'PEP', 'T', 'CRM',
# 'INTC', 'ORCL','CSCO', 'TMO', 'AVGO', 'ACN', 'QCOM', 'DHR',

tickerList = ['AAPL','AMZN', 'GOOGL', 'AAPL', 'MSFT', 'V', 'MA', 'PG', 'DIS', 'CMCSA', 'KO', 'ADBE', 'NKE', 'PEP', 'T', 'CRM',
 'INTC', 'ORCL', 'CSCO', 'TMO', 'AVGO', 'ACN', 'QCOM', 'DHR', 'VZ', 'NVDA']

quartilList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

data = []
for ticker in tickerList:
    dateList = Helper_functions.get_list_of_dates(ticker)
    i = 0
    while i < len(dateList):
        Stock1 = Stock(ticker, dateList[i], quartilList[i])

        print("Company:                             " + ticker)
        print("     Date:                                " + dateList[i])
        print("capitalExpenditures:                 " + Stock1.capitalExpenditures)
        print("     Stcok Price:                         " + str(Stock1.stockPrice))
        print("Return on Investment:                " + Stock1.returnOnInvestment)
        print("     TotalLiabilities:                    " + str(Stock1.totalLiabilities))
        print("Price per earnings:                  " + str(Stock1.pricePerEarnings))
        print("     Book Value per Share:                " + str(Stock1.bookValuePerShare))
        print("Price per Book Ratio per Share:       " + str(Stock1.pricePerBookRatioPerShare))
        print("Test Balance_Sheet ass" + str(Stock1.esgRating))

        i += 1



