from Stock import Stock
import Helper_functions
import seaborn as sns
import matplotlib.pyplot as plt


tickerList = ['AMZN', 'GOOGL', 'AAPL', 'MSFT', 'V', 'JNJ', 'MA', 'PG', 'DIS']

quartilList = ['1', '5', '9', '13', '17', '21', '25', '29', '33', '37', '41']

data = []
for ticker in tickerList:
    dateList = Helper_functions.get_list_of_dates(ticker)
    i = 0
    while i < len(dateList):
        Stock1 = Stock(ticker, dateList[i], quartilList[i])
        print("capitalExpenditures: " + Stock1.capitalExpenditures + "vom " + dateList[i] + "Company: " + ticker)
        #print("Price per Ratio of the Companny:" + Stock1.symbole + " in quartyl " + Stock1.quarterly + " was: " + Stock1.pricePerEarnings)
        #print("Company: " + stock + "Date: " + dateList[i] + " Stcok Price: " + str(Stock1.stockPrice))
        #print("Company: " + stock + "Date: " + dateList[i] + "Return on Investment: " + Stock1.returnOnInvestment)
        print("Company: " + ticker + "Date: " + dateList[i] + "Return on Investment: " + Stock1.returnOnInvestment)
        #print("Company: " + stock + "Date: " + dateList[i] + "Return on Investment: " + Stock1.)
        i += 1



