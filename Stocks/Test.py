from Stock import Stock
import Helper_functions
import seaborn as sns
import matplotlib.pyplot as plt

#companys with missing values (teh number in front of the Tiker is the index in the DB:
# 6('JNJ'), (9'HD'), (10'PYPL'),(11'VZ'), (16MRK no data in 2020)

# past already 'AMZN', 'GOOGL', 'AAPL', 'MSFT', 'V', 'MA', 'PG', 'DIS', 'CMCSA', 'KO', 'ADBE', 'NKE', 'PEP', 'T',
tickerList = [
                 'CRM', 'INTC', 'ORCL', 'ABT', 'CSCO', 'ABBV', 'AVGO', 'ACN',
              'QCOM', 'LLY', 'DHR', 'UN']

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
        print("     TotalLiabilities:                    " + Stock1.totalLiabilities)
        print("Price per earnings:                  " + Stock1.pricePerEarnings)
        print("     Book Value per Share:                " + str(Stock1.bookValuePerShare))
        print("Price per Book Ratio per Share:       " + str(Stock1.pricePerBookRatioPerShare))
        print()
        i += 1



