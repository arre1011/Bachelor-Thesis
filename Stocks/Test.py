from Stock import Stock
import seaborn as sns
import matplotlib.pyplot as plt

stocksList = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'V', 'JNJ', 'MA', 'PG', 'DIS']

dateList = ['2020-09-30', '2019-09-30', '2018-09-30', '2017-09-30', '2016-09-30', '2015-09-30', '2014-09-30',
            '2013-09-30', '2012-09-30', '2011-09-30']
quartilList = ['1', '5', '9', '13', '17', '21', '25', '29', '33', '37', '41']

print("####################################")
data = []
for stock in stocksList:
    i = 0
    while i < len(dateList):
        Stock1 = Stock(stock, dateList[i], quartilList[i])
        #print("capitalExpenditures: " + Stock1.capitalExpenditures + "vom " + dateList[i] + "Company: " + stock)
        #print("Price per Ratio of the Companny:" + Stock1.symbole + " in quartyl " + Stock1.quarterly + " was: " + Stock1.pricePerEarnings)
        #print("Company: " + stock + "Date: " + dateList[i] + " Stcok Price: " + str(Stock1.stockPrice))
        print("Company: " + stock + "Date: " + dateList[i] + "Return on Investment: " + Stock1.returnOnInvestment)

        i += 1



